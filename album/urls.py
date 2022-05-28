from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='album_home'),
    path('all/', views.all_images, name='album_all')
]
