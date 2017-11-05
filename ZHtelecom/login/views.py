#coding:utf-8
#from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext,loader

# Create your views here.
def loginui(request):
    # tmp=loader.get_template('login/login.html')
    # return HttpResponse(tmp.render())
    return render(request,'login/login.html')

