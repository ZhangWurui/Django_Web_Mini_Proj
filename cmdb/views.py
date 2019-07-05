from django.shortcuts import render
from django.http import HttpResponseRedirect
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

def home(request):
    return HttpResponseRedirect("/home/")

def goHome(request):
    return render(request, "home.html")

def worldCloud(request):
    return HttpResponseRedirect("/worldcloud/")

def goWorldCloud(request):
    return render(request, "worldcloud.html")

def filmreview(request):
    return HttpResponseRedirect("/filmreview/")

def goFilmReview(request):
    ctx = {}
    with open( 'static/temp/temp.txt', mode='r', encoding='UTF-8') as f_in:
        ctx['rlt'] = f_in.readlines()
    return render(request, "filmreview.html", ctx)