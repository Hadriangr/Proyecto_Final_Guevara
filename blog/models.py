# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.CharField(max_length=100, default='-')
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=255, default='-')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='imgs/', blank=True, null=True)

    
    def __str__(self):
        return self.titulo


class Avatar(models.Model):
    user = models.OneToOneField(User, related_name='avatar_blog', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/')