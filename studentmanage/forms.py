from django import forms

from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","email","phone", "courses"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "bg-white max-w-[100%] max-[375px]:block ml-0 min-[375px]:ml-2 my-2 rounded text-black"}),
            "email": forms.EmailInput(attrs={"class": "bg-white max-w-[100%] max-[375px]:block ml-0 min-[375px]:ml-3 my-2 rounded text-black"}),
            "phone": forms.TextInput(attrs={"class": "bg-white max-w-[100%] max-[375px]:block min-[375px]:ml-1 my-2 rounded text-black"}),
            "courses": forms.CheckboxSelectMultiple(attrs={"class": "max-w-[100%] inline-block ml-4 text-left"})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "code", "public"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "bg-white max-w-[100%] my-2 max-[375px]:block rounded text-black"}),
            "code": forms.TextInput(attrs={"class": "bg-white max-w-[100%] my-2 ml-1 max-[375px]:block max-[375px]:ml-0 rounded text-black"}),
            "public": forms.CheckboxInput(attrs={"class": "bg-white max-w-[100%] inline-block ml-4 text-left"})
        }
