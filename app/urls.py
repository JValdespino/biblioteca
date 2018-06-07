
from django.urls import path
from . import views

urlpatterns = [
    path('lector/consulta',views.consultalector),
    path('guardarlector',views.guardarlector),
    path('lector',views.lector),
    path('visita/consulta', views.consultaVisita),
    path('guardaVisita', views.guardaVisita),
    path('visita', views.visita),
    path('', views.index),
    
]
