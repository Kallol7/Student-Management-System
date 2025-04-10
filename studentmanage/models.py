from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20, unique=True)
    public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(
        max_length=24,
        error_messages={"incomplete": "Enter a phone number."},
        validators=[RegexValidator(r"^[0-9]{10,15}$", "Enter a valid phone number.")],
    )
    courses = models.ManyToManyField(Course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
