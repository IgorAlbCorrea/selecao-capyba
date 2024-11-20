
from django.urls import path
from django.contrib.auth import views as auth_views
from app_cad_usuarios import views

urlpatterns = [
    # página inicial
    path('', views.home, name='home'),

    # Listagem de usuários
    path('usuarios/', views.usuarios, name='listagem_usuarios'),

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Alteração de senha
    path('alterar_senha/', views.AlterarSenhaView.as_view(), name='alterar_senha'),
]
