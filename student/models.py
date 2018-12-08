from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Student(AbstractUser):
    num = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=16)
    sex_choice = (('男', "man"), ('女', "women"))
    sex = models.CharField(max_length=10, choices=sex_choice)
    age = models.IntegerField(default=0)
    settime = models.DateTimeField(auto_now_add=True)
    addr = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    course = models.OneToOneField(to="Course", to_field="num", null=True)
    classes = models.ForeignKey(to="Class", to_field="num", null=True)
    teacher = models.ForeignKey(to="Teacher", to_field="num", null=True)

    def __str__(self):
        return self.num


class Course(models.Model):
    num = models.AutoField(primary_key=True)
    english = models.IntegerField(default=0)
    chinese = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    phycics = models.IntegerField(default=0)

    def __str__(self):
        return self.chinese


class Class(models.Model):
    num = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    teachers = models.ForeignKey(to="Teacher",to_field="num", null=True)

    def __str__(self):
        return self.cname


class Teacher(models.Model):
    num = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=16)
    age = models.IntegerField(default=0)
    sex_choice = (("男", "man"), ("女", "woman"))
    sex = models.CharField(max_length=10, choices=sex_choice)
    phone = models.CharField(max_length=32)
    
    def __str__(self):
        return self.tname