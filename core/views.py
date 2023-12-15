from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = "core/index.html"


class CategoriaCreateView(generic.CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categoria_listar")


class CategoriaListView(generic.ListView):
    model = Categoria


class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categorias_listar")


class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy("core:categoria_listar")
