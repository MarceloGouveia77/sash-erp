from django.forms import model_to_dict
from django.http import JsonResponse
from api.decorators import auth_required
from api.exceptions import Exceptions
from api.serializers.rh import serializer_funcionario, serializer_funcionario_list
from rh.models import Departamento, Funcao, Funcionario
from django.views.decorators.http import require_http_methods
import json

exceptions = Exceptions()

@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def funcoes(request, usuario = None, pk = None):
    if request.method == "GET":
        funcoes = list(Funcao.objects.all().values())
        return JsonResponse(funcoes, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            funcao = model_to_dict(Funcao.objects.create(**dados))
            return JsonResponse(funcao, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            funcao = model_to_dict(Funcao.objects.get(id=pk))
            Funcao.objects.filter(id=pk).delete()
            return JsonResponse(funcao, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Função informada não existe.'}, status=400)

@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def departamentos(request, usuario = None, pk = None):
    if request.method == "GET":
        departamentos = list(Departamento.objects.all().values())
        return JsonResponse(departamentos, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            departamento = model_to_dict(Departamento.objects.create(**dados))
            return JsonResponse(departamento, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            departamento = model_to_dict(Departamento.objects.get(id=pk))
            Departamento.objects.filter(id=pk).delete()
            return JsonResponse(departamento, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Departamento informado não existe.'}, status=400)


@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def funcionarios(request, usuario = None, pk = None):
    if request.method == "GET" and pk:
        try:
            funcionario = serializer_funcionario(Funcionario.objects.get(id=pk))
            return JsonResponse(funcionario, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': 'Funcionário informado não existe.'}, status=400)
        
    if request.method == "GET":
        funcionarios = serializer_funcionario_list(Funcionario.objects.all())
        return JsonResponse(funcionarios, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            funcionario = serializer_funcionario(Funcionario.objects.create(**dados))
            return JsonResponse(funcionario, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            funcionario = serializer_funcionario(Funcionario.objects.get(id=pk))
            Funcionario.objects.filter(id=pk).delete()
            return JsonResponse(funcionario, safe=False, status=200)
        except Exception as e:
            return exceptions.objeto_nao_existe("Funcionário")
