from django.views import generic
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = "index.html"


class Administrativo(generic.TemplateView):
    template_name = "adimnistrativo.html"


class CategoriaCreateView(generic.CreateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categoria_listar")
    template_name = "categorias/categoria_form.html"


class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = "categorias/categoria_list.html"


class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy("core:categoria_listar")
    template_name = "categorias/categoria_form.html"


class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy("core:categoria_listar")
