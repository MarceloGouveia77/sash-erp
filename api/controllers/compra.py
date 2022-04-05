from django.forms import model_to_dict
from django.http import JsonResponse
from api.decorators import auth_required
from api.exceptions import Exceptions
from django.views.decorators.http import require_http_methods
from api.serializers.compra import serializer_compra, serializer_compra_item, serializer_compra_item_list, serializer_compra_list
from compra.models import Compra, CompraItem, Fornecedor
import json

exceptions = Exceptions()

@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def compra_items(request, usuario = None, pk = None):
    if request.method == "GET" and pk:
        try:
            compra_item = serializer_compra_item(CompraItem.objects.get(id=pk))
            return JsonResponse(compra_item, safe=False, status=200)
        except:
            return exceptions.objeto_nao_existe("CompraItem")
    
    if request.method == "GET":
        compra_items = serializer_compra_item_list(CompraItem.objects.all())
        return JsonResponse(compra_items, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            compra_item = serializer_compra_item(CompraItem.objects.create(**dados))
            return JsonResponse(compra_item, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            compra_item = serializer_compra_item(CompraItem.objects.get(id=pk))
            CompraItem.objects.filter(id=pk).delete()
            return JsonResponse(compra_item, safe=False, status=200)
        except Exception as e:
            return exceptions.objeto_nao_existe("CompraItem")

@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def compras(request, usuario = None, pk = None):
    if request.method == "GET" and pk:
        try:
            compra = serializer_compra(Compra.objects.get(id=pk))
            return JsonResponse(compra, safe=False, status=200)
        except:
            return exceptions.objeto_nao_existe("Compra")
    
    if request.method == "GET":
        compras = serializer_compra_list(Compra.objects.all())
        return JsonResponse(compras, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            compra = serializer_compra(Compra.objects.create(**dados))
            return JsonResponse(compra, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            compra = serializer_compra(Compra.objects.get(id=pk))
            Compra.objects.filter(id=pk).delete()
            return JsonResponse(compra, safe=False, status=200)
        except Exception as e:
            return exceptions.objeto_nao_existe("Compra")
        
@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def fornecedores(request, usuario = None, pk = None):
    if request.method == "GET" and pk:
        try:
            fornecedor = model_to_dict(Fornecedor.objects.get(id=pk))
            return JsonResponse(fornecedor, safe=False, status=200)
        except:
            return exceptions.objeto_nao_existe("Fornecedor")
    
    if request.method == "GET":
        fornecedores = list(Fornecedor.objects.all().values())
        return JsonResponse(fornecedores, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            fornecedor = model_to_dict(Fornecedor.objects.create(**dados))
            return JsonResponse(fornecedor, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            fornecedor = model_to_dict(Fornecedor.objects.get(id=pk))
            Fornecedor.objects.filter(id=pk).delete()
            return JsonResponse(fornecedor, safe=False, status=200)
        except Exception as e:
            return exceptions.objeto_nao_existe("Fornecedor")