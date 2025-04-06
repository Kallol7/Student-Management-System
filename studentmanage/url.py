from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.students, name="students"),
    path("students/add/", views.student_form, name="student_form"),
    path("students/update/<int:pk>/", views.update_student, name="update_student"),
    path("students/delete/<int:pk>/", views.delete_student, name="delete_student"),
    path("courses/", views.courses, name="courses"),
    path("courses/add/", views.course_form, name="course_form"),
    path("courses/update/<int:pk>/", views.update_course, name="update_course"),
    path("courses/delete/<int:pk>/", views.delete_course, name="delete_course")
]
