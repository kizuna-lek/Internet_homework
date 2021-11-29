from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from dormitory import models
from django.http import JsonResponse


#记得改写，此处应该为room_num加起来
@login_required
def hello(request):
    current_user = request.user
    name = models.UserInfo.objects.get(stu_num = current_user.username).name
    dor_list = []
    dor_num = [5,8,9,13,14]
    for i in dor_num:
        temp = {}
        temp.update({"dormitory_num":i})
        if i == 8 or i == 9:
            temp.update({"remarks":"仅供男生选择"})
        else:
            temp.update({"remarks":"无"})
        release = models.RoomNum.objects.filter(dormitory_num=i)
        release_room = 0
        for j in release:
            release_room = release_room + j.free_beds
        temp.update({"release_room":release_room})
        dor_list.append(temp)
    return render(request,"hello.html",{"name":name,"dor_list":dor_list})

@login_required
def logout(request):
    auth.logout(request)
    return redirect("/login")

@login_required
def chooseajax(request):
    result = {"code":999,"msg":""}
    current_user = request.user
    stu_num = current_user.username
    stu_male = models.UserInfo.objects.get(stu_num=stu_num).male
    dor_num = eval(request.POST.get("dor_num"))

    if models.UserInfo.objects.get(stu_num=stu_num).havedor:
        result = {"code":1004,"msg":"您已经抢到宿舍，无法复抢"}
        return JsonResponse(result)

    row_roommate = []
    row_roommate.append(request.POST.get("room_mate1"))
    row_roommate.append(request.POST.get("room_mate2"))
    row_roommate.append(request.POST.get("room_mate3"))

    temp_roommate = []
    for i in row_roommate:
        if i:
            temp_roommate.append(i)
    room_mate = []
    for i in temp_roommate:
        if models.UserInfo.objects.filter(stu_num=i):
            room_mate.append(i)
    if len(temp_roommate) != len(room_mate):
        result = {"code":1001,"msg":"您输入的队友学号有误，请重新输入"}
        return JsonResponse(result)

    for i in room_mate:
        if stu_male != models.UserInfo.objects.get(stu_num=i).male:
            result = {"code":1002,"msg":"不支持异性组队，请重新选择队友"}
            return JsonResponse(result)

    for i in room_mate:
        if models.UserInfo.objects.get(stu_num=i).havedor:
            result = {"code":1005,"msg":"您的队友已经抢到宿舍，无法复抢"}
            return JsonResponse(result)

    #往下才开始写数据库，上述错误不计入订单
    room_list = models.RoomNum.objects.filter(dormitory_num = dor_num)
    for i in room_list:
        if i.free_beds >= len(room_mate)+1:
            result = {"code":1000,"msg":"恭喜您，抢宿舍成功!"}
            room_id = i.id
            room_name = i.room_name
            break
    if(result["code"] != 1000):
        #床位不足的订单要插入订单表
        models.Order.objects.create(stu_num = stu_num, dormitory_num=dor_num,male=stu_male,people_num=len(room_mate)+1, is_correct = False)
        result = {"code":1003,"msg":"空余床位不足，抢宿舍失败，请减少队伍人数或选择其他宿舍楼"}
        return JsonResponse(result)

    #下面为抢到宿舍，要修改的一些列数据库
    #user_info表
    user_havedor = models.UserInfo.objects.get(stu_num = stu_num)
    user_havedor.havedor = True
    user_havedor.save()
    for i in room_mate:
        user_havedor = models.UserInfo.objects.get(stu_num = i)
        user_havedor.havedor = True
        user_havedor.save()

    #order表
    models.Order.objects.create(stu_num = stu_num, dormitory_num=dor_num,male=stu_male,people_num=len(room_mate)+1, is_correct = True)

    #order_info表
    if len(room_mate) == 1:
        models.OrderInfo.objects.create(stu_num=stu_num,room_name=room_name,room_mate1=room_mate[0])
    elif len(room_mate) == 2:
        models.OrderInfo.objects.create(stu_num=stu_num,room_name=room_name,room_mate1=room_mate[0],room_mate2=room_mate[1])
    elif len(room_mate) == 3:
        models.OrderInfo.objects.create(stu_num=stu_num,room_name=room_name,room_mate1=room_mate[0],room_mate2=room_mate[1],room_mate3=room_mate[2])
    else:
        models.OrderInfo.objects.create(stu_num=stu_num,room_name=room_name)

    #room_num表
    room = models.RoomNum.objects.get(id = room_id)
    room.free_beds = room.free_beds - len(room_mate) -1
    room.save()

    #Room_stu_info表
    try:
        room_stu = models.RoomStuInfo.objects.get(room_id=room_id)
        for i in range(len(room_mate)+1):
            if room_stu.room_mate1:
                room_stu.room_mate1 = room_mate[i]
                break
            if room_stu.room_mate2:
                room_stu.room_mate2 = room_mate[i]
                break
            if room_stu.room_mate3:
                room_stu.room_mate3 = room_mate[i]
                break
            if room_stu.room_mate4:
                room_stu.room_mate4 = room_mate[i]
                break
            if room_stu.room_mate5:
                room_stu.room_mate5 = room_mate[i]
                break
            if room_stu.room_mate6:
                room_stu.room_mate6 = room_mate[i]
        room_stu.save()
    except models.RoomStuInfo.DoesNotExist:
        if len(room_mate) == 0:
            models.RoomStuInfo.objects.create(room_id=room_id, room_name=room_name,room_mate1 = stu_num)
        elif len(room_mate) == 1:
            models.RoomStuInfo.objects.create(room_id=room_id, room_name=room_name,room_mate1=stu_num,room_mate2=room_mate[0])
        elif len(room_mate) == 2:
            models.RoomStuInfo.objects.create(room_id=room_id, room_name=room_name,room_mate1 = stu_num,room_mate2=room_mate[0],room_mate3=room_mate[1])
        else:
            models.RoomStuInfo.objects.create(room_id=room_id, room_name=room_name,room_mate1 = stu_num,room_mate2=room_mate[0],room_mate3=room_mate[1],room_mate4=room_mate[2])

    return JsonResponse(result)

@login_required
def result(request):
    return render(request,"result.html")
