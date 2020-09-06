from django.http import HttpResponse
from django.shortcuts import render

def about(response):
    return render(response,'about.html')

def home(response):
    return render(response,'home.html')