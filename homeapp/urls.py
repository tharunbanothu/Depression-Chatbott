from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home_about',views.home_about,name='home_about'),
    path('home_contact',views.home_contact,name='home_contact'),
]