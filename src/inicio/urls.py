from django.urls import path
from .views import Inicio, AcercaDe

app_name = 'inicio'

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("acerca-de", AcercaDe.as_view(), name="acerca-de"),

]