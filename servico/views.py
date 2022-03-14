from ast import Delete
from django.http import JsonResponse
from django.shortcuts import redirect, render
from servico.models import Servico
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