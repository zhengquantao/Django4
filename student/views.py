from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from student import forms
from student import models

# Create your views here.


def login(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        tname = models.Teacher.objects.values('tname')
        # print(tname.values(), tname)
        # print(user)
        if user:
            if username in [i['tname'] for i in tname]:
                auth.login(request, user)
                ret["msg"] = "/teacher/index/"
            else:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)  # 将登录用户赋值给request.user
                ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            ret["status"] = 1
            ret["msg"] = "用户名或者密码错误！"
            return JsonResponse(ret)

    return render(request, 'login.html')


def register(request):
    form_obj = forms.RegForm()
    if request.method == "POST":
        form_obj = forms.RegForm(request.POST)
        # 让form帮我们做效验
        if form_obj.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            addr = request.POST.get("addr")
            phone = request.POST.get("phone")

            models.Student.objects.create_user(username=username, password=password, sex=gender, age=age, addr=addr, phone=phone)
            return redirect("/login/")
    return render(request, "register.html", {"form_obj": form_obj})


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


@login_required
def index(request):
    # print(request.user.username)
    user_message = models.Student.objects.filter(num=request.user.num).first()
    
    return render(request, "index.html", {"user_message": user_message})


def course(request, pk):
    # print(pk)
    class_message = models.Student.objects.filter(course_id=pk).first()
    # print(class_message)
    return render(request, 'course.html', {"class_message": class_message})


def classes(request, pk):
    print(pk)
    class_message = models.Student.objects.filter(classes_id=pk).first()
    # print(class_message)
    
    return render(request, 'classes.html', {"class_message": class_message,})