from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def printerr(request):
    return HttpResponse("Hello, World!")

def test(request):
    return HttpResponse("success")
