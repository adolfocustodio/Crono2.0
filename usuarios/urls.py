from django.urls import include, path
from . import views


app_name = "usuarios"
urlpatterns = [
   path('usuario/criar/', views.UsuarioCreateView.as_view(), name='usuario_criar'),
   path('usuario/listar/', views.UsuarioListView.as_view(), name='usuario_listar'),
   path('usuario/detalhes/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detalhes'),
   path('usuario/excluir/<int:pk>/', views.UsuarioDeleteView.as_view(), name='usuario_excluir'),
   path('accounts/', include('django.contrib.auth.urls'))
]
