from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from compra.models import Compra, CompraItem
from compra.forms import CompraForm
from almox.models import Item

# Create your views here.

def index(request):
    compras = Compra.objects.all()
    return render(request, 'compras/index.html', {'compras': compras})

def cadastrar(request):
    form = CompraForm(request.POST or None)
    data = {
        'form': form
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("compra:editar", compra_id=instance.id)
    
    return render(request, 'compras/cadastrar.html', data)

def editar(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    itens_compra = CompraItem.objects.filter(compra=compra.id)
    
    data = {
        'compra': compra,
        'itens': Item.objects.all(),
        'itens_compra': itens_compra
    }
    return render(request, 'compras/editar.html', data)

def adicionar_item_compra(request):
    if request.method == "POST":
        compra_id = int(request.POST.get("compra_id"))
        item_id = int(request.POST.get("item_id"))
        quantidade = float(request.POST.get("item_quantidade"))
        valor = float(request.POST.get("item_valor"))
        estoque = bool(request.POST.get("estoque"))
        
        CompraItem.objects.create(
            compra_id=compra_id,
            item_id=item_id,
            quantidade=quantidade,
            valor=valor,
            estoque=estoque
        )
        return JsonResponse({'msg': 'Item adicionado com sucesso'}, status=201)
    return JsonResponse({'error': 'Método não permitido'}, status=405)