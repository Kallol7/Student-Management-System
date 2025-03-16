from django import forms

from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","email","phone", "courses"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "my-2 ml-1 rounded text-black"}),
            "email": forms.TextInput(attrs={"class": "my-2 ml-2 rounded text-black"}),
            "courses": forms.CheckboxSelectMultiple(attrs={"class": "inline-block ml-4 text-left"}),
            "phone": forms.TextInput(attrs={"class": "my-2 ml-0 rounded text-black"}),
        }
