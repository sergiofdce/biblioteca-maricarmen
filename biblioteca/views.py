from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return render(response,"index.html")


def hello(response):
    return render(response,"hello.html")

