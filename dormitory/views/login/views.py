from django.shortcuts import render
from django.contrib import auth
from django.http import JsonResponse

def login(request):
    return render(request, "login.html")


def loginajax(request):
    result = {"code":1000,"msg":""}
    stu_num = request.POST.get("stu_num")
    password = request.POST.get("password")

    if stu_num and password:
        user = auth.authenticate(username=stu_num, password=password)
        if user:
            auth.login(request,user)
            result = {"code":1000,"msg":"登录成功"}
        else:
            result = {"code":1001,"msg":"用户名或者密码输入错误"}
    else:
        result = {"code":1002,"msg":"学号或者密码为空"}

    return JsonResponse(result)
