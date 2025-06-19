from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views

urlpatterns =  [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('testimonial', views.testimonial,name='testimonial'),
    path('contact', views.contact,name='contact'),
    path('blog', views.blog,name='blog'),
]
