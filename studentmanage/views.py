from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm
from django.http import HttpResponse
from .models import Student, Course
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "studentmanage/index.html")

@login_required
def student_form(request, success=None):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.created_by = request.user
            entry.save()
            form = StudentForm()
            success = True
        else:
            success = False
    if success is None:
        form = StudentForm()
    
    return render(request, "studentmanage/studentform.html", {"form": form, "success": success, "verb": "added"})

@login_required
@ensure_csrf_cookie
def students(request):
    students = Student.objects.filter(created_by=request.user).prefetch_related("courses").order_by("-updated_at")
    response = [{
        "id": student.pk,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "courses": [course for course in student.courses.all()]
    } for student in students]

    return render(request, "studentmanage/students.html", {"students": response})

@login_required
def update_student(request, pk, success=None):
    try:
        student = Student.objects.get(pk=pk, created_by=request.user)
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

@login_required
@require_POST
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk, created_by=request.user)
        student.delete()
        return HttpResponse(content="Successfully deleted pk", status=200)
    except:
        return render(request, "studentmanage/basemsg.html", {"message": f"Student {pk} not found"})

@login_required
def course_form(request, success=None):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            form = CourseForm()
            success = True
        else:
            success = False
    if success is None:
        form = CourseForm()
    
    return render(request, "studentmanage/courseform.html", {"form": form, "success": success, "verb": "added"})

@ensure_csrf_cookie
def courses(request):
    user = request.user
    if user.is_authenticated:
        courses = Course.objects.filter(created_by=user)
    else:
        courses = Course.objects.filter(public = True)
    
    response = [{
        "id": course.pk,
        "name": course.name,
        "code": course.code
    } for course in courses]

    return render(request, "studentmanage/courses.html", {"courses": response})

@login_required
def update_course(request, pk, success=None):
    try:
        student = Course.objects.get(pk=pk, created_by=request.user)
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

@login_required
@require_POST
def delete_course(request, pk):
    try:
        course = Course.objects.get(pk=pk, created_by=request.user)
        course.delete()
        return HttpResponse(content="Successfully deleted pk", status=200)
    except:
        return render(request, "studentmanage/basemsg.html", {"message": f"Course {pk} not found"})
