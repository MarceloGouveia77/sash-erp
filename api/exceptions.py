

from django.http import JsonResponse


class Exceptions():
    
    def __init__(self) -> None:
        pass
    
    def objeto_nao_existe(obj):
        return JsonResponse({'error': f'{obj} informado não existe.'}, status=400)