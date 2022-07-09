from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=200)
	texto = models.TextField()
	imagen = models.ImageField(upload_to='imagen_nota')
	fecha = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.titulo