
from django.urls import path
from . import views


urlpatterns = [
    path('guardaVisita', views.guardaVisita),
    path('visita/editarV', views.editaVisita),
    path('visita/regVisita', views.regVisita),
    path('regMenu', views.regresaMenu),
    path('visita/modificarVisita', views.modificaVisita),
    path('visita/consulta', views.consultaVisita),
    path('visita', views.visita),
    path('visita/elimi', views.elimi),
    

    path('guardaLibro',views.guardaLibro),
    path('lector',views.lector),
    path('prestamos',views.prestamos),
    path('guardarprestamos',views.guardarprestamos),
    path('guardarlector',views.guardarlector),
    #path('consultaInt', views.consultas_int),
    path('', views.index),
    
]