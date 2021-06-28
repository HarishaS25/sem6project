from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='taskmanager-home'),
    path('about/', views.about, name='taskmanager-about')
]
