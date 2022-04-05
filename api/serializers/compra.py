from django.forms import model_to_dict

from api.serializers.almox import serializer_item

def serializer_compra(compra):
    compra_json = model_to_dict(compra)
    compra_json['solicitante'] = {'id': compra.solicitante.id, 'nome': compra.solicitante.nome, 'cpf': compra.solicitante.cpf}
    compra_json['fornecedor'] = model_to_dict(compra.fornecedor)
    compra_json['centro_custo'] = {'id': compra.centro_custo.id, 'nome': compra.centro_custo.nome}
    
    return compra_json

def serializer_compra_list(compras):
    compras_json = []
    for compra in compras:
        compra = serializer_compra(compra)
        compras_json.append(compra)
    return compras_json

def serializer_compra_item(compra_item):
    compra_item_json = model_to_dict(compra_item)
    compra_item_json['compra'] = serializer_compra(compra_item.compra)
    compra_item_json['item'] = serializer_item(compra_item.item)
    return compra_item_json

def serializer_compra_item_list(compra_items):
    compra_items_json = []
    for compra_item in compra_items:
        compra_item = serializer_compra_item(compra_item)
        compra_items_json.append(compra_item)
    return compra_items_json