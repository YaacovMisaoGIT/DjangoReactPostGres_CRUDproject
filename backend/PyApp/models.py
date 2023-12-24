from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=20)
    Registration = models.CharField(max_length=10)
    Email = models.CharField(max_length=20)
    Course = models.CharField(max_length=50)