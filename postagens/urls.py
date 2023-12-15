from django.urls import path
from . import views


app_name = 'postagens'
urlpatterns = [
    path('postagem/criar/', views.PostagemCreateView.as_view(), name='postagem_criar'),
    path('postagem/editar/<int:pk>/', views.PostagemUpdateView.as_view(), name='postagem_editar'),
    path('postagem/excluir/<int:pk>/', views.PostagemDeleteView.as_view(), name='postagem_excluir')
]
