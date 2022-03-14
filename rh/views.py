from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rh.models import FolhaPagamento, Funcionario
from rh.forms import CadastrarFuncionarioForm
from django.views.decorators.csrf import csrf_exempt
import xlsxwriter
import io

def funcionarios(request):
    funcionarios = Funcionario.objects.filter(ativo=True)
    
    data = {
        'funcionarios': funcionarios
    }
    
    return render(request, 'rh/funcionarios/index.html', data)

def cadastrar_funcionario(request):
    form = CadastrarFuncionarioForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('rh:funcionarios')
    else:
        return render(request, 'rh/funcionarios/cadastrar.html', {'form': form, 'errors': form.errors})

def editar_funcionario(request, funcionario_id):
    funcionario = Funcionario.objects.get(id=funcionario_id)
    form = CadastrarFuncionarioForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('rh:funcionarios')
    return render(request, 'rh/funcionarios/editar.html', {'form': form, 'funcionario': funcionario})

@csrf_exempt
def excluir_funcionario(request, funcionario_id):
    if request.method == "DELETE":
        Funcionario.objects.get(id=funcionario_id).delete()
        return JsonResponse({'msg': 'Funcionário excluido com sucesso'}, status=200)
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
def exportar_funcionarios(request):
    if request.user.is_authenticated:
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        
        linha = 0
        
        header_format = workbook.add_format({'bold': True, 'bg_color': '#FFB900'})
        worksheet.write(linha, 0, "Código", header_format)
        worksheet.write(linha, 1, "Nome", header_format)
        worksheet.write(linha, 2, "CPF", header_format)
        worksheet.write(linha, 3, "Departamento", header_format)
        worksheet.write(linha, 4, "Admissão", header_format)
        worksheet.write(linha, 5, "Demissão", header_format)
        worksheet.write(linha, 6, "Email", header_format)
        worksheet.write(linha, 7, "Ativo", header_format)
        worksheet.write(linha, 8, "Celular", header_format)
        
        funcionarios = Funcionario.objects.all()
        for f in funcionarios:
            linha += 1
            worksheet.write(linha, 0, f.id)
            worksheet.write(linha, 1, f.nome)
            worksheet.write(linha, 2, f.cpf)
            worksheet.write(linha, 3, f.departamento.nome)
            worksheet.write(linha, 4, f.obter_data_admissao())
            worksheet.write(linha, 5, f.obter_data_demissao())
            worksheet.write(linha, 6, f.email)
            worksheet.write(linha, 7, f.ativo)
            worksheet.write(linha, 8, f.celular)
            
        workbook.close()
        response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="funcionarios.xls"'
        output.close()
        return response
    return JsonResponse({'erro': 'Não autorizado'}, status=401)
    
def folha_pagamento(request):
    if request.method == "POST":
        mes = int(request.POST.get("mes"))
        ano = int(request.POST.get("ano"))
        
        data = datetime(year=ano, month=mes, day=1).date()
        funcionarios = Funcionario.objects.all()
        for funcionario in funcionarios:
            try:
                folha = FolhaPagamento.objects.get(
                    funcionario=funcionario,
                    mes=data,
                )
                folha.save() # Atualizando calculos
            except:
                FolhaPagamento.objects.create(
                    funcionario=funcionario,
                    mes=data,
                )
        folhas_pagamento = FolhaPagamento.objects.filter(mes__year=data.year, mes__month=data.month)
        return render(request, 'rh/folha/index.html', {'folhas': folhas_pagamento, 'mes': mes, 'ano': ano})
        
    return render(request, 'rh/folha/index.html', {})

@csrf_exempt
def fechar_folha_pagamento(request):
    if request.method == "POST":
        mes = int(request.POST.get("mes"))
        ano = int(request.POST.get("ano"))
        
        data = datetime(year=ano, month=mes, day=1).date()
        folhas_pagamento = FolhaPagamento.objects.filter(mes__year=data.year, mes__month=data.month)
        for folha in folhas_pagamento:
            folha.fechada = True
            folha.save()
        return JsonResponse({'msg': 'Folha fechada com sucesso'}, status=200)
    else:
        return JsonResponse({'erro': 'Método não suportado.'}, status=405)