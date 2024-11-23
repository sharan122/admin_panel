from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def printerr(request):
    return HttpResponse("Hello, World!")

def test(request):
    return HttpResponse("success")
def test2(request):
    return HttpResponse("testing purpose")



def drf_rabeeh(request):
    return HttpResponse('Hello rabeeh')
def vaishnav(req):
    return HttpResponse('vaishnav')

def sharan(request):
    return HttpResponse("testing purpose sharan")
