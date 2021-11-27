from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from dormitory.models import UserInfo

def register(request):
    return render(request,"register.html")

#把学号当作用户名
def registerajax(request):
    result = {"code":1000,"msg":""}
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        stu_num = request.POST.get("stu_num")
        male_info = request.POST.get("male")
        if male_info == "男":
            male = True
        else:
            male = False
        if stu_num and password and male_info and name:
            user_list = User.objects.filter(username=stu_num)
            if user_list:
                result = {"code":1001,"msg":"用户已存在"}
            else:
                user = User.objects.create_user(username=stu_num, password=password)
                user_info = UserInfo.objects.create(stu_num=stu_num, name=name, male = male)
                result = {"code":1000,"msg":"注册成功"}
        else:
            result = {"code":1002,"msg":"输入信息不能为空","male_info":male_info}
    return JsonResponse(result)




