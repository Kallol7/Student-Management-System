from django import forms

from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","email","phone", "courses"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "max-w-[100%] my-2 ml-1 rounded text-black"}),
            "email": forms.EmailInput(attrs={"class": "max-w-[100%] my-2 ml-2 rounded text-black"}),
            "courses": forms.CheckboxSelectMultiple(attrs={"class": "max-w-[100%] inline-block ml-4 text-left"}),
            "phone": forms.TextInput(attrs={"class": "max-w-[100%] my-2 ml-0 rounded text-black"}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "code", "public"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "max-w-[100%] my-2 ml-1 rounded text-black"}),
            "code": forms.TextInput(attrs={"class": "max-w-[100%] my-2 ml-2 rounded text-black"}),
            "public": forms.CheckboxInput(attrs={"class": "max-w-[100%] inline-block ml-4 text-left"})
        }
