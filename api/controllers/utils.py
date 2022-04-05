from django.http import JsonResponse
import jwt
from django.conf import settings

def _nao_autorizado():
    return JsonResponse({'error':'Usuário não autorizado'}, status=401)

def obter_token(request):
    token = str(request.headers['Authorization']).split(" ")[1]
    return token

def obter_decode_token(request):
    token = str(request.headers['Authorization']).split(" ")[1]
    return jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])