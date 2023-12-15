from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path('admin/', admin.site.urls)
]
