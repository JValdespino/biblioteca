
from django.urls import path
from . import views

urlpatterns = [
    path('visita', views.visita),
    path('', views.index),
]
