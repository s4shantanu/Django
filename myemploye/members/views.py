from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return HttpResponse('<h1>About Page1</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Page2</h1>')