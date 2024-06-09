from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("read/<int:pk>" , views.read, name="read"),  
    path("newpage", views.newpage, name="newpage"),
    path("input", views.input, name="input"),   
]

