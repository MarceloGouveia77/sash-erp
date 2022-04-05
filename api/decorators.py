

from django.http import JsonResponse
from core.models import User
from django.views.decorators.csrf import csrf_exempt

def auth_required(func):
    def wrapper(request, *args, **kwargs):
        jwt = str(request.headers['Authorization']).split(" ")[1]
        try:
            usuario = User.objects.get(token=jwt)
            return func(request, usuario, *args, **kwargs)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Token Inválido'}, status=401)
    return wrapper