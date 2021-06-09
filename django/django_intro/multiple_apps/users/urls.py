from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('users/new_route', views.new),
    path('users', views.index),
]