from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('hello world!')
    #대소문자 틀리면 안됨 HttpResponse
    #http에서 alt + enter누르면 뭐가 뜸