from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'taskmanager/home.html')


def about(request):
    return render(request, 'taskmanager/about.html')


def tasks(request):
    return render(request, 'taskmanager/tasks.html')
