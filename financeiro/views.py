from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from financeiro.models import ContasPagar, Movimentacao, Pagamentos
import datetime

# Create your views here.

def movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-id')
    data = { 'movimentacoes': movimentacoes }
    return render(request, 'financeiro/movimentacoes.html', data)

def contas_pagar(request):
    contas = ContasPagar.objects.all()
    data = { 'contas': contas, 'tab_contas': 'active' }
    return render(request, 'financeiro/contas.html', data)

@csrf_exempt
def obter_pagamentos_conta(request, conta_id):
    if request.method == 'GET':
        pagamentos = Pagamentos.objects.filter(conta_id=conta_id)
        
        pagamentos_json = []
        for pagamento in pagamentos:
            pagamentos_json.append({
                'vencimento': pagamento.obter_vencimento(),
                'descricao': pagamento.descricao,
                'valor': f'R$ {pagamento.valor:.2f}',
                'pago': pagamento.pago,
            })
        
        return JsonResponse(pagamentos_json, status=200, safe=False)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def pagar(request, pagina):
    if pagina == "pendentes":
        pagamentos = Pagamentos.objects.filter(pago=False)
        data = {'pagamentos': pagamentos, 'tab_pagar': 'active'}
        template = 'financeiro/pagar.html'
    elif pagina == "historico":
        pagamentos = Pagamentos.objects.filter(pago=True)
        data = {'pagamentos': pagamentos, 'tab_historico': 'active'}
        template = 'financeiro/historico.html'
    else:
        return HttpResponseNotFound('Página não encontrada')
    
    data['pagina'] = pagina
    if request.method == "GET" and request.GET.get("data-inicial"):
        data_inicial = datetime.datetime.strptime(request.GET.get("data-inicial"), "%Y-%m-%d")
        data_final = datetime.datetime.strptime(request.GET.get("data-final"), "%Y-%m-%d")

        data['data_inicial'] = data_inicial.strftime("%Y-%m-%d")
        data['data_final'] = data_final.strftime("%Y-%m-%d")
        data['pagamentos'] = pagamentos.filter(vencimento__gte=data_inicial, vencimento__lte=data_final.replace(hour=23, minute=59, second=59))
        
    data['valor_total'] = sum([p.valor for p in data['pagamentos']])
    return render(request, template, data)

@csrf_exempt
def pagar_conta(request):
    if request.method == "POST":
        pagamento_id = int(request.POST.get("pagamento_id"))
        data = datetime.datetime.strptime(request.POST.get("data_pagamento"), "%Y-%m-%d")
        
        pagamento = Pagamentos.objects.get(id=pagamento_id)
        pagamento.pagar_conta(data)
        
        return JsonResponse({'msg': 'Pagamento efetuado com sucesso'}, status=200) 
    return JsonResponse({'error': 'Método não autorizado'}, status=405) 