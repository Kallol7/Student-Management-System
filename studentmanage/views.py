from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseNotFound
from .models import Student, Course

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

def students(request):
    students = Student.objects.prefetch_related("courses")
    response = [{
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "courses": [course for course in student.courses.all()]
    } for student in students]

    return render(request, "studentmanage/students.html", {"students": response})

def update_student(request, pk, success=None):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    
    try:
        student = Student.objects.get(pk=pk)
        form = StudentForm(instance=student)
    except:
        return render(request, "studentmanage/notfound.html", {"pk": pk})
    
    return render(request, "studentmanage/studentform.html", {"form": form, "success": success})
