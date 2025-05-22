from django.shortcuts import render, redirect
from .forms import PedidoForm, SaborPizzaForm, PizzaFormSet
from .models import Pedido, Pizza
from django.forms import formset_factory

def fazer_pedido_view(request):
    SaborFormSet = formset_factory(SaborPizzaForm, extra=0)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        quantidade = int(request.POST.get('quantidade', 1))
        sabor_formset = SaborFormSet(request.POST, prefix='sabores')

        if pedido_form.is_valid() and sabor_formset.is_valid():
            pedido = Pedido.objects.create(
                nome=pedido_form.cleaned_data['nome'],
                cpf=pedido_form.cleaned_data['cpf'],
                endereco=pedido_form.cleaned_data['endereco'],
                quantidade=quantidade,
                borda=pedido_form.cleaned_data['borda'],
                tamanho=pedido_form.cleaned_data['tamanho'],
                sabor1='01'  # valor fictício
            )

            for sabor_form in sabor_formset:
                Pizza.objects.create(
                    pedido=pedido,
                    sabor=sabor_form.cleaned_data['sabor']
                )

            return redirect('pedido_confirmado')
    else:
        pedido_form = PedidoForm()
        sabor_formset = SaborFormSet(prefix='sabores')

    return render(request, 'cliente/fazer_pedido.html', {
        'form': pedido_form,
        'sabor_formset': sabor_formset,
    })

def pedido_confirmado_view(request):
    return render(request, 'cliente/pedido_confirmado.html')

def fila_pedidos_view(request):
    pedidos = Pedido.objects.all().order_by('-id')
    return render(request, 'funcionario/fila_pedidos.html', {'pedidos': pedidos})