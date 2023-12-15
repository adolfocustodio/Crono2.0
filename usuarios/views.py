from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.permissions import AdministradorPermission
from .models import Usuario
from .forms import UserRegistrationForm
from django.urls import reverse_lazy


class UsuarioCreateView(generic.CreateView):
    model = Usuario
    form_class = UserRegistrationForm
    success_url = reverse_lazy("core:home")


class UsuarioListView(generic.ListView, LoginRequiredMixin, AdministradorPermission):
    model = Usuario


class UsuarioDetailView(generic.ListView, LoginRequiredMixin, AdministradorPermission):
    model = Usuario


class UsuarioDeleteView(generic.DeleteView, LoginRequiredMixin, AdministradorPermission):
    model = Usuario
    success_url = reverse_lazy("usuarios:usuario_listar")
