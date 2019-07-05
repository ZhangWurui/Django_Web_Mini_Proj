# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponseRedirect
 
# 接收POST请求数据
def filmreview_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['content']
        print(type(ctx['rlt']))
        with open( 'static/temp/temp.txt', mode='w+', encoding='UTF-8') as f_out:
            f_out.write(ctx['rlt'])
    return render(request, "filmreview.html", ctx)