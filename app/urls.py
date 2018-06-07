
from django.urls import path
from . import views

urlpatterns = [
    path('guardaLibro',views.guardaLibro),
    path('libro',views.libro),
    path('guardarlector',views.guardarlector),
    path('lector',views.lector),
    path('visita/consulta', views.consultaVisita),
    path('guardaVisita', views.guardaVisita),
    path('visita', views.visita),
    path('', views.index),
    
]
