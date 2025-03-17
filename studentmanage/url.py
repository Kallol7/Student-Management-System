from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.students, name="students"),
    path("students/add/", views.student_form, name="student_form"),
    path("students/update/<int:pk>/", views.update_student, name="update_student"),
    path("students/delete/<int:pk>/", views.delete_student, name="delete_student")
]
