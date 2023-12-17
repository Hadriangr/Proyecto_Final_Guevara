# myblog/urls.py
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls import handler404,handler500
from blog.views import pagina_error, error_servidor
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    re_path(r'^.*/$', pagina_error, name='pagina_no_encontrada'),
]

if settings.DEBUG:
   
    handler500 = error_servidor
else:
    handler500 = 'blog.views.error_servidor'
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
