# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponseRedirect
 
# 接收POST请求数据
def filmreview_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['content']
    return render(request, "filmreview.html", ctx)