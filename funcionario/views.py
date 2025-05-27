from django.shortcuts import render, redirect
from cliente.models import Pedido
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Funcionario
from django.contrib.auth.hashers import make_password


def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('id')  # Ordem crescente, do mais antigo para o mais novo
    return render(request, 'funcionario/listar_pedidos.html', {'pedidos': pedidos})

def processar_pedido_view(request):
    if request.method == "POST":
        pedido = Pedido.objects.first()
        if pedido:
            pedido.delete()
            messages.success(request, "Pedido processado com sucesso.")
        else:
            messages.warning(request, "Nenhum pedido para processar.")
    return redirect('listar_pedidos')

def logar_func(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('listar_pedidos')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'funcionario/login.html')

def registrar_funcionario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se já existe
        if Funcionario.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já registrado.")
        elif Funcionario.objects.filter(email=email).exists():
            messages.error(request, "Email já registrado.")
        else:
            funcionario = Funcionario(
                nome=nome,
                cpf=cpf,
                email=email,
                senha=make_password(senha)
            )
            funcionario.save()
            messages.success(request, "Funcionário registrado com sucesso!")
            return redirect('login_funcionario')  # ajusta se seu nome de URL for outro

    return render(request, 'funcionario/registro.html')