from django.forms import model_to_dict
from django.http import JsonResponse
from api.decorators import auth_required
from api.exceptions import Exceptions
from django.views.decorators.http import require_http_methods
from cliente.models import Cliente
import json

exceptions = Exceptions()

@require_http_methods(["POST", "GET", "DELETE"])
@auth_required
def clientes(request, usuario = None, pk = None):
    if request.method == "GET" and pk:
        try:
            cliente = cliente = model_to_dict(Cliente.objects.get(id=pk))
            return JsonResponse(cliente, safe=False, status=200)
        except:
            return exceptions.objeto_nao_existe("Cliente")
    
    if request.method == "GET":
        clientes = list(Cliente.objects.all().values())
        return JsonResponse(clientes, safe=False, status=200)
    
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            cliente = model_to_dict(Cliente.objects.create(**dados))
            return JsonResponse(cliente, safe=False, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    if request.method == "DELETE":
        try:
            cliente = model_to_dict(Cliente.objects.get(id=pk))
            Cliente.objects.filter(id=pk).delete()
            return JsonResponse(cliente, safe=False, status=200)
        except Exception as e:
            return exceptions.objeto_nao_existe("Cliente")