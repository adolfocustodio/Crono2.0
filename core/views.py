from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.permissions import AdministradorPermission
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = "index.html"


class CategoriaCreateView(generic.CreateView, LoginRequiredMixin, AdministradorPermission):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categoria_listar")
    template_name = "categorias/categoria_form.html"


class CategoriaListView(generic.ListView, LoginRequiredMixin, AdministradorPermission):
    model = Categoria
    template_name = "categorias/categoria_list.html"


class CategoriaUpdateView(generic.UpdateView, LoginRequiredMixin, AdministradorPermission):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categoria_listar")
    template_name = "categorias/categoria_form.html"


class CategoriaDeleteView(generic.DeleteView, LoginRequiredMixin, AdministradorPermission):
    model = Categoria
    success_url = reverse_lazy("core:categoria_listar")
