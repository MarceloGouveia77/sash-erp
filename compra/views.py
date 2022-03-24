from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from compra.models import Compra, CompraItem
from compra.forms import CompraForm
from financeiro.models import Pagamentos
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
    
    if compra.concluida:
        pagamentos = Pagamentos.objects.filter(conta__compra=compra)
        data['pagamentos'] = pagamentos
        
    return render(request, 'compras/editar.html', data)

@csrf_exempt
def concluir_compra(request):
    if request.method == "POST":
        compra_id = request.POST.get("compra_id")
        compra = Compra.objects.get(id=int(compra_id))
        compra.concluida = True
        compra.inicializar_pagamentos()
        compra.save()
        
        return JsonResponse({'msg': 'Compra finalizada com sucesso'}, status=200)
    return JsonResponse({'error': 'Método não permitido'}, status=405)
    

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

@csrf_exempt
def alterar_quantidade_item_compra(request):
    if request.method == "POST":
        compra_item_id = request.POST.get("compra_item_id")
        qtde = request.POST.get("qtde")
        
        compra_item = CompraItem.objects.get(id=int(compra_item_id))
        compra_item.alterar_quantidade(float(qtde))
        
        data = {
            "msg": "Alterado com sucesso",
            'compra_item_total': format(compra_item.valor_total, '.2f'),
            'compra_valor_total': format(compra_item.compra.valor_total, '.2f'),
            'qtde': format(compra_item.quantidade, '.2f')
        }
        
        return JsonResponse(data, status=200)
    return JsonResponse({"error": "Método não permitido"})

@csrf_exempt
def remover_item_compra(request, compra_item_id):
    if request.method == "DELETE":
        compra_item = CompraItem.objects.get(id=int(compra_item_id))
        compra = compra_item.compra
        CompraItem.objects.get(id=int(compra_item_id)).delete()
        compra.recalcular_valor_total()
        return JsonResponse({'msg': 'Item removido com sucesso'}, status=200)
    return JsonResponse({"error": "Método não permitido"})
    