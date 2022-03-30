from ast import Delete
from django.http import JsonResponse
from django.shortcuts import redirect, render
from almox.models import SaidaItem
from servico.models import OrdemServico, Servico, ServicosOS
from servico.forms import ServicoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    servicos = Servico.objects.all()
    
    data = {
        'servicos': servicos
    }
    
    return render(request, 'servico/index.html', data)

def cadastrar(request):
    form = ServicoForm(request.POST or None)
    
    data = {
        'form' : form
    }
    if form.is_valid():
        form.save()
        return redirect('servico:index')
    return render(request, 'servico/cadastrar.html', data)

def editar(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    form = ServicoForm(request.POST or None, instance=servico)
    
    data = {
        'form' : form
    }
    if form.is_valid():
        form.save()
        return redirect('servico:index')
    return render(request, 'servico/editar.html', data)

@csrf_exempt    
def deletar(request, servico_id):
    if request.method=='DELETE':
        Servico.objects.get(id=servico_id).delete()
        return JsonResponse({'msg':'Serviço deletado com sucesso'}, status=200)
    else:
        return JsonResponse({'error':'Método não permitido'}, status=405)
    
def detalhe_os(request, os_id):
    os = OrdemServico.objects.get(id=os_id)
    servicos_os = ServicosOS.objects.filter(os=os)
    saidas = SaidaItem.objects.filter(saida__os=os)
    
    total_servicos, total_saidas = 0, 0
    
    for servico in servicos_os:
        total_servicos += servico.obter_valor()
        
    for saida in saidas:
        total_saidas += saida.obter_valor()
    
    data = {
        'os': os,
        'servicos_os': servicos_os,
        'saidas': saidas,
        'total_servicos': total_servicos,
        'total_saidas': total_saidas,
        'total_os': (total_servicos + total_saidas)
    }
    
    return render(request, 'os/detalhe.html', data)

def os(request):
    ordens = OrdemServico.objects.all()
    
    data = {
        'ordens': ordens
    }
    return render(request, 'os/index.html', data)