from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/add", views.student_form, name="student_form")
]
