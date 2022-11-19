from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    
    path('add/', views.add, name='add'),
    path('detail/<int:diary_id>', views.detail, name='detail'),
    path('diarylist/', views.diarylist, name='diarylist'),
  
]