from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hello(request):
    return render(request,"hello.html")
