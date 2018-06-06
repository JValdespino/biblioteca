
from django.urls import path
from . import views

urlpatterns = [
    path('modificar/', views.modificar),
    path('editar', views.modificacion),
    path('consulta', views.consulta),
    path('guardarPersona', views.guardarPersona),
    path('sumar', views.sumar),
    path('esclava', views.esclava),
    path('', views.index),
    path('nombre', views.nombre),
]
