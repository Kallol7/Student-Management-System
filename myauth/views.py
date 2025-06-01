from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm
from .user_routing import get_user_bucket
from django.conf import settings
import secrets
import requests
from google.oauth2.id_token import verify_oauth2_token
from google.auth.transport import requests as google_requests

def signup(request, success = None):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/login/?signed_up_user={form.instance.username}")
        else:
            success = False
    
    if success is None:
        form = UserRegistrationForm()
    
    return render(request, "myauth/signup.html", {"form": form, "success": success})

def userlogin(request, success=None):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect("/")
            next = request.GET.get("next")
            if next is not None:
                response = redirect(next)
            
            # Nginx logic, to always send the user to the same server.
            response.set_cookie("user_bucket", get_user_bucket(username))
            
            return response
        else:
            form = LoginForm(request.POST)
            success = False
    
    if success is None:
        username = request.GET.get("signed_up_user")
        form = LoginForm({
            "username": username
        })
        if username is not None:
            success = True
    
    return render(request, "myauth/login.html", {"form": form, "success": success, "username": username})

def userlogout(request):
    logout(request)
    response = redirect("/")
    response.delete_cookie('user_bucket')
    
    return response

def loginwithgoogle(request):
    state = secrets.token_urlsafe(22)
    nonce = secrets.token_urlsafe(16)
    
    request.session["state"] = state
    request.session["nonce"] = nonce
    
    scope = "openid profile email"
    
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        f"&client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&scope={scope}"
        f"&state={state}"
        f"&nonce={nonce}"
    )

    return redirect(auth_url)

def oauth2callback(request):
    returned_state = request.GET.get("state")
    expected_state = request.session.get("state")
    if not returned_state or returned_state != expected_state:
        return HttpResponse("Invalid state parameter", status=400)

    code = request.GET.get("code")
    if not code:
        return HttpResponse("No authorization code provided", status=400)

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = requests.post(token_url, data=token_data)
    if token_response.status_code != 200:
        return HttpResponse("Token exchange failed", status=400)
    
    token_json = token_response.json()
    
    id_token_str = token_json.get("id_token")
    access_token = token_json.get("access_token")
    
    if not id_token_str or not access_token:
        return HttpResponse("Missing tokens in response", status=400)
    
    try:
        id_info = verify_oauth2_token(
            id_token_str,
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=settings.SKEW_IN_SECONDS
        )
    except ValueError:
        return HttpResponse(f"Invalid ID token", status=400)
    
    expected_nonce = request.session.get("nonce")
    if id_info.get("nonce") != expected_nonce:
        return HttpResponse("Invalid nonce", status=400)
    
    email = id_info.get("email")
    name = id_info.get("name")
    if not email:
        return HttpResponse("Email not found in ID token", status=400)

    user, _ = User.objects.get_or_create(
        username=email,
        email=email,
        defaults={"first_name": name or ""}
    )
    login(request, user)

    request.session.pop("state", None)
    request.session.pop("nonce", None)

    return redirect("/")
