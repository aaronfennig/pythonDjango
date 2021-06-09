from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('process_money', views.process_money, name = 'process_gold'),
    path('reset_game', views.reset_game),
]