# blog/urls.py
from django.urls import path
from .views import  post_list, Crearblogview,index, about, post, contact,PostDetailView

urlpatterns = [
    path('crear_blog/', Crearblogview.as_view(), name='crear_blog'),  
    path('post_list/', post_list, name='post_list'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('contact/', contact, name='contact'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
