from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm
from django.http import HttpResponse
from .models import Student, Course

def home(request):
    return render(request, "studentmanage/index.html")

def student_form(request, success=None):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            success = True
        else:
            success = False
    if success is None:
        form = StudentForm()
    
    return render(request, "studentmanage/studentform.html", {"form": form, "success": success, "verb": "added"})

def students(request):
    students = Student.objects.prefetch_related("courses").order_by("-updated_at")
    response = [{
        "id": student.pk,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "courses": [course for course in student.courses.all()]
    } for student in students]

    return render(request, "studentmanage/students.html", {"students": response})

def update_student(request, pk, success=None):
    try:
        student = Student.objects.get(pk=pk)
        form = StudentForm(instance=student)
    except:
        return render(request, "studentmanage/basemsg.html", {"notfound": pk})
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    
    return render(request, "studentmanage/studentform.html", {"form": form, "success": success, "verb": "updated"})

def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return HttpResponse(content="Successfully deleted pk",status = [200])
    except:
        return render(request, "studentmanage/basemsg.html", {"message": f"Student {pk} not found"})

def course_form(request, success=None):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
            success = True
        else:
            success = False
    if success is None:
        form = CourseForm()
    
    return render(request, "studentmanage/courseform.html", {"form": form, "success": success, "verb": "added"})

def courses(request):
    courses = Course.objects.all()
    response = [{
        "id": course.pk,
        "name": course.name,
        "code": course.code
    } for course in courses]

    return render(request, "studentmanage/courses.html", {"courses": response})

def update_course(request, pk, success=None):
    try:
        student = Course.objects.get(pk=pk)
        form = CourseForm(instance=student)
    except:
        return render(request, "studentmanage/basemsg.html", {"notfound": pk})
    
    if request.method == "POST":
        form = CourseForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            success = True
        else:
            success = False
    
    return render(request, "studentmanage/courseform.html", {"form": form, "success": success, "verb": "updated"})

def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course.delete()
        return HttpResponse(content="Successfully deleted pk",status = [200])
    except:
        return render(request, "studentmanage/basemsg.html", {"message": f"Course {pk} not found"})
