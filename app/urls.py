
from django.urls import path
from . import views

urlpatterns = [
    path('libro/elimina', views.eliminaLibro),
    path('libro/modificarLibro', views.modificaLibro),
    path('libro/edita', views.libroEdita),
    path('libro/consulta', views.libroConsulta),
    path('libro', views.libro),
    path('guardaVisita', views.guardaVisita),
    path('visita/editarV', views.editaVisita),
    path('visita/regVisita', views.regVisita),
    path('regMenu', views.regresaMenu),
    path('visita/modificarVisita', views.modificaVisita),
    path('visita/consulta', views.consultaVisita),
    path('visita', views.visita),
    path('visita/elimi', views.elimi),
    path('lector/consulta',views.consultalector),
    path('lector/eliminar',views.eliminar),
    path('lector/modificarLector',views.modificarLector),
    path('lector/editarlec',views.editarlec),
    path('guardaLibro',views.guardaLibro),
    path('lector',views.lector),
    path('prestamos',views.prestamos),
    path('guardarprestamos',views.guardarprestamos),
    path('guardarlector',views.guardarlector),
    #path('consultaInt', views.consultas_int),
    path('', views.index),
    
]
