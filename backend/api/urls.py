from django.contrib import admin
from django.urls import path, include
from .views import CdrCreateView


urlpatterns = [
    path('get/', CdrCreateView.as_view()),
]