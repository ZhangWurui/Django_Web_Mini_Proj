from django.shortcuts import render

# Create your views here.
from cmdb import models

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        pwd = request.POST.get("pwd",None)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=pwd)
        # 从数据库里读取数据
        user_list = models.UserInfo.objects.all()
    return render(request, "index.html",{"data":user_list})
    