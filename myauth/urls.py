from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup_form"),
    path("login/", views.userlogin, name="login_form"),
    path("logout/", views.userlogout, name="user_logout"),
    path("login-google/", views.loginwithgoogle, name="login_with_google"),
    path("callback/", views.oauth2callback, name="callback_google"),
]
