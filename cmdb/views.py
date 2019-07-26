from django.shortcuts import render
from django.http import HttpResponseRedirect
from cmdb.db_util import *
from cmdb.methods import *

# def index(request):
#     if request.method == "POST":
#         username = request.POST.get("username",None)
#         pwd = request.POST.get("pwd",None)
#         # 添加数据到数据库
#         models.UserInfo.objects.create(user=username,pwd=pwd)
#     # 从数据库里读取数据
#     user_list = models.UserInfo.objects.all()
#     return render(request, "index.html",{"data":user_list})

def welcome(request):
    return render(request, "welcome.html")

def home(request):
    return HttpResponseRedirect("/home/")

def goHome(request):
    message = ""
    emotion = ""
    reply = ""
    if request.method == "POST":
        message = request.POST.get("message", None)
        emotion, replies = judgeEmotion(message)
        print(emotion)
        if len(replies) > 0:
            reply = replies[0]
        else:
            reply = 'null'
        print(reply)
    return render(request, "home.html", {'emotion':emotion, 'reply':reply})

def goTech(request):
    return render(request, "tech.html")

def goFilmReview(request):
    film_reviews = searchAllFilmReview()
    return render(request, "filmreview.html", {'film_reviews':film_reviews})

def goFilmReviewSpeci(request):
    if request.method == "GET":
        id = request.GET.get("id", 0)
        film_review = searchFilmReviewById(id)
    return render(request, "filmreviewspeci.html", {'film_review':film_review})