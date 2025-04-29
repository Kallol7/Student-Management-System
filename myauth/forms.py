from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# DSHFdfxs1234
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # solves pain in the ash
        self.fields.get("username").widget.attrs.update({"class": "bg-white block w-full my-1 max-w-[100%] rounded"})
        self.fields.get("email").widget.attrs.update({"class": "bg-white block w-full my-1 max-w-[100%] rounded"})
        self.fields.get("password1").widget.attrs.update({"class": "bg-white block w-full my-1 max-w-[100%] rounded"})
        self.fields.get("password2").widget.attrs.update({"class": "bg-white block w-full my-1 max-w-[100%] rounded"})

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "bg-white block sm:inline-block max-sm:w-full my-1 sm:mb-3 max-w-[100%] rounded"}),
            "password": forms.PasswordInput(attrs={"class": "bg-white block sm:inline-block max-sm:w-full my-1 sm:ml-[4.8px] max-w-[100%] rounded"})
        }
