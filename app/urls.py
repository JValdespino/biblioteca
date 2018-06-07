
from django.urls import path
from . import views

urlpatterns = [
    path('guardaVisita', views.guardaVisita),
    path('visita', views.visita),
    path('', views.index),
]
