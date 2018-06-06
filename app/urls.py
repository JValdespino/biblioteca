
from django.urls import path
from . import views

urlpatterns = [
    path('esclava', views.esclava),
    path('', views.index),
]
