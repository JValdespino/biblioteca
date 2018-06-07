
from django.urls import path
from . import views

urlpatterns = [
    path('guardaVisita', views.guardaVisita),
    path('visita/consulta', views.consultaVisita),
    path('visita', views.visita),
    path('visita/elimi', views.elimi),


    path('guardaLibro',views.guardaLibro),
    path('libro',views.libro),
    path('guardarlector',views.guardarlector),
    path('lector',views.lector),
    path('consultaInt', views.consultas_int),
    path('', views.index),
    
]
