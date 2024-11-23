from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def printerr(request):
    return HttpResponse("Hello, World!")

def test(request):
    return HttpResponse("success")
def test2(request):
    return HttpResponse("testing purpose")

def nanda_kishor(request):
    return HttpResponse("Nandu bhaii")
