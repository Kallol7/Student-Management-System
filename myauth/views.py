from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, LoginForm
from .user_routing import get_user_bucket

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
