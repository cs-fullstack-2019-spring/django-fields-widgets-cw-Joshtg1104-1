from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heroApp/', views.heroApp, name='heroApp'),
    path('congrats/', views.heroApp, name='congrats'),
]
