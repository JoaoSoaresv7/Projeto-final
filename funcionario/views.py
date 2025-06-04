<<<<<<< HEAD
from django.shortcuts import render, redirect
from cliente.models import Pedido
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Funcionario
from django.shortcuts import get_object_or_404
from .models import Funcionario, Etiqueta


def listar_pedidos(request):
    # Verifica se o funcionário está logado
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    pedidos = Pedido.objects.all().order_by('id')
    return render(request, 'funcionario/listar_pedidos.html', {'pedidos': pedidos})

def processar_pedido_view(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

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
        email = request.POST.get('username')  # pode mudar para 'email'
        senha = request.POST.get('senha')

        try:
            funcionario = Funcionario.objects.get(email=email)
            if check_password(senha, funcionario.senha):
                request.session['funcionario_id'] = funcionario.id
                messages.success(request, 'Login realizado com sucesso.')
                return redirect('home_page')
            else:
                messages.error(request, 'Senha incorreta.')
        except Funcionario.DoesNotExist:
            messages.error(request, 'Funcionário não encontrado.')

    return render(request, 'funcionario/login.html')

def registrar_funcionario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

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
            return redirect('login_funcionario')

    return render(request, 'funcionario/registro.html')

def home_page(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    pedidos = Pedido.objects.all().order_by('id')
    return render(request, 'funcionario/home_page.html', {'pedidos': pedidos})

def logout_funcionario(request):
    request.session.flush()  # limpa a sessão
    messages.success(request, "Logout realizado com sucesso.")
    return redirect('login_funcionario')

def concluir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.concluido = True
    pedido.save()
    messages.success(request, f'Pedido de {pedido.nome} marcado como concluído.')
    return redirect('home_page')

def excluir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    Etiqueta.objects.create(pedido=pedido, acao="Pedido excluído")
    pedido.delete()
    messages.success(request, "Pedido excluído e etiqueta criada.")
=======
from django.shortcuts import render, redirect
from cliente.models import Pedido
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Funcionario
from django.shortcuts import get_object_or_404
from .models import Funcionario, Etiqueta


def listar_pedidos(request):
    # Verifica se o funcionário está logado
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    pedidos = Pedido.objects.all().order_by('id')
    return render(request, 'funcionario/listar_pedidos.html', {'pedidos': pedidos})

def processar_pedido_view(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

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
        email = request.POST.get('username')  # pode mudar para 'email'
        senha = request.POST.get('senha')

        try:
            funcionario = Funcionario.objects.get(email=email)
            if check_password(senha, funcionario.senha):
                request.session['funcionario_id'] = funcionario.id
                messages.success(request, 'Login realizado com sucesso.')
                return redirect('home_page')
            else:
                messages.error(request, 'Senha incorreta.')
        except Funcionario.DoesNotExist:
            messages.error(request, 'Funcionário não encontrado.')

    return render(request, 'funcionario/login.html')

def registrar_funcionario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

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
            return redirect('login_funcionario')

    return render(request, 'funcionario/registro.html')

def home_page(request):
    if 'funcionario_id' not in request.session:
        return redirect('login_funcionario')

    pedidos = Pedido.objects.all().order_by('id')
    return render(request, 'funcionario/home_page.html', {'pedidos': pedidos})

def logout_funcionario(request):
    request.session.flush()  # limpa a sessão
    messages.success(request, "Logout realizado com sucesso.")
    return redirect('login_funcionario')

def concluir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.concluido = True
    pedido.save()
    messages.success(request, f'Pedido de {pedido.nome} marcado como concluído.')
    return redirect('home_page')

def excluir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    Etiqueta.objects.create(pedido=pedido, acao="Pedido excluído")
    pedido.delete()
    messages.success(request, "Pedido excluído e etiqueta criada.")
>>>>>>> 81e4968abde002e858a3addca30aac4f09a89e45
    return redirect('home_page')