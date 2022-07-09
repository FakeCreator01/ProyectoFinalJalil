from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Inicio(TemplateView):
	template_name = 'inicio.html'



class AcercaDe(TemplateView):
	template_name = 'acerca-de.html'