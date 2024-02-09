from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, "index.html")

def cyberprotection(request):
    return TemplateResponse(request, "theory.html")

def mentors(request):
    return TemplateResponse(request, "mentors.html")

def event1(request):
    return TemplateResponse(request, "event1.html")

def result1(request):
    return TemplateResponse(request, "result1.html")

def event2(request):
    return TemplateResponse(request, "event2.html")

def result2(request):
    return TemplateResponse(request, "result2.html")

def end(request):
    return TemplateResponse(request, "end.html")