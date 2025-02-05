from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Biblioteca Mari Carmen coming soon...")

def hello(response):
    return render(response,"hello.html")
