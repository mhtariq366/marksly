from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    credit_hours = models.PositiveIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course_code} - {self.name}"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username