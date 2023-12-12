# blog/models.py
from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # Corregir el nombre del campo a "title"
    content = models.TextField()
    pub_date = models.DateTimeField('Fecha de Publicación')
    
    def __str__(self):
        return self.title
