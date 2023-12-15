from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('administrativo/', views.Administrativo.as_view(), name='administrativo'),
    path('categoria/criar/', views.CategoriaCreateView.as_view(), name='categoria_form'),
    path('categoria/listar/', views.CategoriaListView.as_view(), name='categoria_listar'),
    path('categoria/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categoria/excluir/<int:pk>/', views.CategoriaDeleteView.as_view(), name='categoria_excluir')
]
