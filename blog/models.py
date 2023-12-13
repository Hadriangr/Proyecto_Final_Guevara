# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100, default='Anonymous')
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=255, default='Autor no agrego subtitulo')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.titulo
