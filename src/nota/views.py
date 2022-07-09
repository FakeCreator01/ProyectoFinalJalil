from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Nota
from .forms import NotaForm

# Create your views here.
class ListaNotas(LoginRequiredMixin, ListView):
	template_name = 'nota/lista-notas.html'
	model = Nota
	context_object_name = 'notas'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notas'] = context['notas'].filter(usuario=self.request.user)	
		
		return context


	#mixins
	login_url = 'usuario/login'
	redirect_field_name = 'usuario/login.html'

class CrearNota(LoginRequiredMixin, CreateView):
	template_name = 'nota/crear-nota.html'
	model = Nota
	form_class = NotaForm
	success_url = reverse_lazy('nota:lista-notas')

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		
		return super(CrearNota, self).form_valid(form)


	#mixins
	login_url = "/usuario/login"
	

class VerNota(LoginRequiredMixin, DetailView):
	template_name = 'nota/ver-nota.html'
	model = Nota

	#mixins
	login_url = '/usuario/login'
	

class EditarNota(LoginRequiredMixin, UpdateView):
	template_name = 'nota/editar-nota.html'
	model = Nota
	form_class = NotaForm
	success_url = reverse_lazy('nota:lista-notas')

	#mixins
	login_url = '/usuario/login'
	

class EliminarNota(LoginRequiredMixin, DeleteView):
	template_name = 'nota/eliminar-nota.html'
	model = Nota
	success_url = reverse_lazy('nota:lista-notas')

	#mixins
	login_url = '/usuario/login'
	


