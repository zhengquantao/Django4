from django.shortcuts import render
from student import models

# Create your views here.


def index(request):
    print(request.user.num)
    teacher = models.Student.objects.filter(num=request.user.num)
    teacher_message = models.Teacher.objects.all()
    return render(request, 't_index.html', {"teacher": teacher, "teacher_message": teacher_message})
