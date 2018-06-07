
from django.urls import path
from . import views

urlpatterns = [
    path('prestamos',views.prestamos),
    path('guardarprestamos',views.guardarprestamos),
    path('guardarlector',views.guardarlector),
    path('lector',views.lector),
    path('visita/consulta', views.consultaVisita),
    path('guardaVisita', views.guardaVisita),
    path('visita', views.visita),
    path('consultaInt', views.consultas_int),
    path('', views.index),
    
]
