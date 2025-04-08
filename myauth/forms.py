from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
        self.fields.get("username").widget.attrs.update({"class": "block w-full my-1 max-w-[100%] my-0 rounded"})
        self.fields.get("email").widget.attrs.update({"class": "block w-full my-1 max-w-[100%] my-0 rounded"})
        self.fields.get("password1").widget.attrs.update({"class": "block w-full my-1 max-w-[100%] my-0 rounded"})
        self.fields.get("password2").widget.attrs.update({"class": "block w-full my-1 max-w-[100%] my-0 rounded"})

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "text-black my-1 max-w-[100%] my-0 rounded max-[375px]:block"}),
            "password": forms.PasswordInput(attrs={"class": "text-black my-1 max-w-[100%] my-0 rounded max-[375px]:block max-[375px]:ml-0 ml-1"})
        }
