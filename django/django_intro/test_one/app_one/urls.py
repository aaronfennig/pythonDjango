from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('csrf', views.csrf),
    path('users', views.create_user),
    path('success', views.show_page),
]