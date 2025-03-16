from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "studentmanage/index.html")

def student_form(request):
    return render(request, "studentmanage/studentform.html")
