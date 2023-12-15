from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('', include('usuarios.urls', namespace='usuarios')),
    path('', include('postagens.urls', namespace='postagens')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
