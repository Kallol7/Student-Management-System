from django.shortcuts import render, redirect
from .forms import StudentForm
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
