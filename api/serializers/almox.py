from django.forms import model_to_dict

def serializer_item(item):
    item_json = model_to_dict(item)
    item_json['categoria'] = {'id': item.categoria.id, 'nome': item.categoria.nome}
    
    return item_json

def serializer_item_list(items):
    items_json = []
    for item in items:
        item = serializer_item(item)
        items_json.append(item)
    return items_json