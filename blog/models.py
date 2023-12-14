# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100, default='-')
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=255, default='-')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.titulo

