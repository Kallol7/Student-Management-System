# Generated by Django 5.1.7 on 2025-03-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanage', '0005_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
