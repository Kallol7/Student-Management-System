from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    return render(request, "studentmanage/index.html")

def student_form(request, success=None):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    if success is None:
        form = StudentForm()

    return render(request, "studentmanage/studentform.html", {"form": form, "success": success})
