from telnetlib import STATUS
from urllib import request
from django.http import HttpResponse, JsonResponse
from api.controllers.utils import obter_decode_token, obter_token
from core.models import User
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def auth(request):
    dados = json.loads(request.body)
    username = dados['username']
    password = dados['password']
    
    try:
        usuario = User.objects.get(username=dados['username'])
        if usuario.auth(username, password):
            return JsonResponse({'jwt_token': usuario.token}, status=200)
        return JsonResponse({'error': 'Usuário ou senha incorretos'}, status=401)
    except:
        return JsonResponse({'error': 'Usuário ou senha incorretos'}, status=401)
    
def logout(request):
    dados = obter_decode_token(request)
    try:
        usuario = User.objects.get(id=dados['id'])
        usuario.token = None
        usuario.save()
        return JsonResponse({'msg': 'Usuário deslogado com sucesso'}, status=200)
    except:
        return JsonResponse({'error': 'Não foi possível realizar o logout.'}, status=400)