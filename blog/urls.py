# blog/urls.py
from django.urls import path
from .views import  post_list, Crearblogview

urlpatterns = [
    path('crear_blog/', Crearblogview.as_view(), name='crear_blog'),  
    path('post_list/', post_list, name='post_list'),
]
