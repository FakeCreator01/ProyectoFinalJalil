from django.urls import path
from .views import ListaNotas, CrearNota, VerNota, EditarNota, EliminarNota

app_name = 'nota'

urlpatterns = [
    path("mis-notas", ListaNotas.as_view(), name="lista-notas"),
    path("crear-nota/", CrearNota.as_view(), name="crear-nota"),
    path("ver-nota/<int:pk>", VerNota.as_view(), name="ver-nota"),
    path("editar-nota/<int:pk>", EditarNota.as_view(), name="editar-nota"),
    path("eliminar-nota/<int:pk>", EliminarNota.as_view(), name="eliminar-nota"),
    
]
