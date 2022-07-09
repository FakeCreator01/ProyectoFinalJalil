from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class Login(LoginView):
	template_name = "usuario/login.html"

class Signup(CreateView):
	template_name = "usuario/signup.html"
	form_class = UserCreationForm
	success_url = reverse_lazy("usuario:login")


