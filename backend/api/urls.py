from django.contrib import admin
from django.urls import path, include
from .views import CdrCreate, CdrList, CdrListById


urlpatterns = [
    path('post/', CdrCreate.as_view()),
    path('get/', CdrList.as_view()),
    path('get/<int:pk>/', CdrListById.as_view())
]