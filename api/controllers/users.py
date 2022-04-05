from django.http import JsonResponse
import json
from api.controllers.utils import _nao_autorizado
from api.decorators import auth_required
from django.views.decorators.http import require_http_methods

from core.models import User

@require_http_methods(["GET"])
@auth_required
def me(request, usuario = None):
    data = {
        'id': usuario.id,
        'username': usuario.username,
        'registro': usuario.date_joined.strftime('%d/%m/%Y as %H:%M'),
        'nome': usuario.first_name,
        'sobrenome': usuario.last_name,
        'admin': usuario.is_superuser,
        'email': usuario.email,
        'ativo': usuario.is_active,
        'ultimo_login': usuario.obter_ultimo_login(),
    }
    return JsonResponse(data, status=200)

@require_http_methods(["GET"])
def obter_usuarios(request):
    usuarios = User.objects.all()
    usuarios_json = []
    
    for usuario in usuarios:
        usuarios_json.append({
            'username': usuario.username,
            'nome': usuario.obter_nome(),
            'ativo': usuario.is_active,
            'membro_desde': usuario.date_joined.strftime("%d/%m/%Y")
        })
    return JsonResponse(usuarios_json, status=200, safe=False)