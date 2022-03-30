from django.http import JsonResponse
from django.shortcuts import redirect, render
from almox.models import Entrada, Item , Saida, EntradaItem, SaidaItem, Emprestimo
from compra.models import Compra, CompraItem
from rh.models import Funcionario
from servico.models import OrdemServico, Servico
import datetime
from django.views.decorators.csrf import csrf_exempt
from almox.forms import ItemForm
# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'almox/index.html', {'items': items})

def detalhe(request, item_id):
    item = Item.objects.get(id=item_id)
    entradas_item = EntradaItem.objects.filter(item=item)
    saidas_item = SaidaItem.objects.filter(item=item)
    emprestimos = Emprestimo.objects.filter(item=item)
    
    data = {
        'item': item,
        'entradas_item': entradas_item,
        'saidas_item': saidas_item,
        'emprestimos': emprestimos
    }
    
    
    return render(request, 'almox/detalhe.html', data)

def cadastrar_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('almox:index')
    return render(request, 'almox/cadastrar_item.html',{'form':form})

def editar_item(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('almox:index')
    return render(request, 'almox/editar_item.html',{'form':form})
    
@csrf_exempt
def deletar_item(request, item_id):
    if request.method=='DELETE':
        Item.objects.get(id=item_id).delete()
        return JsonResponse({'msg':'Item deletado com sucesso'}, status=200)
    else:
        return JsonResponse({'error':'Método não permitido'}, status=405)
    


def entradas(request):
    items = Item.objects.all()
    entradas = EntradaItem.objects.all()
    funcionarios = Funcionario.objects.all()
    servicos = Servico.objects.all()
    
    data = {
        'entradas':entradas,
        'items':items,
        'funcionarios':funcionarios,
        'servicos':servicos
        
    }
    return render(request, 'almox/entradas.html', data)
    
@csrf_exempt
def deletar_entrada(request, entrada_id):
    if request.method=='DELETE':
        EntradaItem.objects.get(id=entrada_id).delete()
        return JsonResponse({'msg':'Entrada deletada com sucesso'}, status=200)
    else:
        return JsonResponse({'error':'Método não permitido'}, status=405)


def saidas(request):
    items = Item.objects.all()
    saidas = SaidaItem.objects.all()
    funcionarios = Funcionario.objects.all()
    ordens = OrdemServico.objects.all()
    
    data = {
        'saidas':saidas,
        'items':items,
        'funcionarios':funcionarios,
        'ordens': ordens
        
    }
    return render(request, 'almox/saidas.html', data)

@csrf_exempt
def adicionar_entrada(request):
    if request.method=='POST':
        data = request.POST.get("data")
        funcionario = request.POST.get("funcionario")
        item_id = request.POST.get("item_id")
        quantidade = request.POST.get("quantidade")
        servico = request.POST.get("servico")
        valor = request.POST.get("valor")
        
        entrada = Entrada(
            data = datetime.datetime.strptime(data, '%Y-%m-%d'),
            funcionario = Funcionario.objects.get(id=int(funcionario)),
            servico = Servico.objects.get(id=int(servico))
        )
        entrada.save()
        
        entrada_item = EntradaItem(
            entrada = entrada,
            item = Item.objects.get(id=int(item_id)),
            quantidade = quantidade,
            valor = valor
        )
        entrada_item.save()
        
        entrada_item.item.entrada_item(float(quantidade))
        
        return JsonResponse({'msg':'Entrada criada com sucesso'})
    return JsonResponse({'error':'Método não permitido'}, status=405)
    
@csrf_exempt
def adicionar_saida(request):
    if request.method=='POST':
        data = request.POST.get("data")
        funcionario = request.POST.get("funcionario")
        item_id = request.POST.get("item_id")
        quantidade = request.POST.get("quantidade")
        os = request.POST.get("os")
        valor = request.POST.get("valor")
        
        try:
            saida = Saida(
                data = datetime.datetime.strptime(data, '%Y-%m-%d'),
                funcionario = Funcionario.objects.get(id=int(funcionario)),
                os = OrdemServico.objects.get(id=int(os))
            )
            saida.save()
            
            saida_item = SaidaItem(
                saida = saida,
                item = Item.objects.get(id=int(item_id)),
                quantidade = quantidade,
                valor = valor
            )
            saida_item.save()
        except Exception as e:
            print (e)
        saida_item.item.saida_item(float(quantidade))
        
        return JsonResponse({'msg':'Saida criada com sucesso'})
    return JsonResponse({'error':'Método não permitido'}, status=405)
    
@csrf_exempt
def deletar_saida(request, saida_id):
    if request.method=='DELETE':
        SaidaItem.objects.get(id=saida_id).delete()
        return JsonResponse({'msg':'Saída deletada com sucesso'}, status=200)
    else:
        return JsonResponse({'error':'Método não permitido'}, status=405)

def recepcao_compras(request):
    compras = Compra.objects.filter(entregue=False)
    
    data = {
        'compras': compras
    }
    return render(request, 'almox/recepcao/index.html', data)

def recepcao(request, compra_id):
    compra = Compra.objects.get(id=int(compra_id))
    compra_itens = CompraItem.objects.filter(compra=compra, recebido=False)
    entradas_itens = EntradaItem.objects.filter(compra_item__compra=compra)
    
    data = {
        'compra': compra,
        'compra_itens': compra_itens,
        'entradas_itens': entradas_itens
    }
    return render(request, 'almox/recepcao/recepcao.html', data)

@csrf_exempt
def receber_item_compra(request):
    if request.method == 'POST':
        compra_item_id = request.POST.get('compra_item_id')
        compra_item = CompraItem.objects.get(id=int(compra_item_id))
        
        hoje = datetime.datetime.today().date()
        
        entrada, created = Entrada.objects.get_or_create(
            compra=compra_item.compra,
            data=hoje,
            funcionario=Funcionario.objects.first(),
            servico=None,
        )
        
        if created:
            entrada = Entrada.objects.get(compra=compra_item.compra)
        
        EntradaItem.objects.create(
            compra_item=compra_item,
            entrada=entrada,
            item=compra_item.item,
            quantidade=compra_item.quantidade,
        )
        compra_item.recebido = True
        compra_item.save()
        return JsonResponse({'msg':'Item recebido'}, status=200)
    return JsonResponse({'error':'Método não permitido'}, status=405)