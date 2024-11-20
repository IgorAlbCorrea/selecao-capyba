from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Usuario

# View para a página inicial
def home(request):
    return render(request, 'usuarios/home.html')

# View para cadastro e listagem de usuários
def usuarios(request):
    # Dados salvos da tela para o BD.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    
    # Todos os usuários cadastrados em uma página nova
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retorna dados p/ a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)

# View para alteração de senha
class AlterarSenhaView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/alterar_senha.html'
    success_url = reverse_lazy('home')  # Redireciona após a alteração bem-sucedida

    def form_valid(self, form):
        messages.success(self.request, 'Sua senha foi alterada com sucesso.')
        return super().form_valid(form)