from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('username',)
