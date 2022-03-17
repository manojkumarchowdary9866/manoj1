from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ipl1(request):
    return HttpResponse('<marquee><h1>march 26</h1><marquee>')
