from django.db import models
from django.core.validators import RegexValidator

class Course(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(
        max_length=24,
        error_messages={"incomplete": "Enter a phone number."},
        validators=[RegexValidator(r"^[0-9]{10,15}$", "Enter a valid phone number.")],
    )
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
