from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')

def welcome(request):
    return HttpResponse('welcome to my app')
def test(request):
    return HttpResponse('This is test')
def factorial(request):
    return HttpResponse('This is factorial')
