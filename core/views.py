from django.views import generic
from postagens.models import Postagem
from usuarios.models import Usuario
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['postagens'] = Postagem.objects.all()

        return context


class Administrativo(generic.TemplateView):
    template_name = "administrativo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['postagens'] = Postagem.objects.count()
        context['categorias'] = Categoria.objects.count()
        context['usuarios'] = Usuario.objects.count()

        return context


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
