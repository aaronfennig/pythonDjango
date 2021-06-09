from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guess', views.guess),
    path('toohigh', views.too_high),
    path('toolow', views.too_low),
    path('youwin', views.you_win),
    path('reset', views.reset),
]