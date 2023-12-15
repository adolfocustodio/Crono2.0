from django.views import generic
from .models import Usuario
from .forms import UserRegistrationForm
from django.urls import reverse_lazy


class UsuarioCreateView(generic.CreateView):
    model = Usuario
    form_class = UserRegistrationForm
    success_url = reverse_lazy("core:home")


class UsuarioListView(generic.ListView):
    model = Usuario


class UsuarioDetailView(generic.ListView):
    model = Usuario


class UsuarioDeleteView(generic.DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuarios:usuario_listar")
