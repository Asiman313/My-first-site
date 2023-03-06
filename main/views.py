from django.shortcuts import render
from django.http import HttpResponse

def index(reqvest):
    return render(reqvest, "main/index.html")

def about(reqvest):
    return render(reqvest, "main/about.html")
