from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('post_dojo', views.postDojo),
    path('post_ninja', views.postNinja),
    path('delete_ninja', views.deleteNinja),
    path('delete_dojo', views.deleteDojo),
]