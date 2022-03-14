from django.shortcuts import render
from almox.models import Item
# Create your views here.

def index(request):
    items = Item.objects.all()
    return render(request, 'almox/index.html', {'items': items})

def detalhe(request, item_id):
    item = Item.objects.get(id=item_id)
    
    data = {
        'item': item
    }
    
    return render(request, 'almox/detalhe.html', data)