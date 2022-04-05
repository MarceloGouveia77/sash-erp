from django.forms import model_to_dict

def serializer_funcionario(funcionario):
    funcionario_json = model_to_dict(funcionario)
    funcionario_json['funcao'] = model_to_dict(funcionario.funcao)
    funcionario_json['departamento'] = model_to_dict(funcionario.departamento)
    return funcionario_json

def serializer_funcionario_list(funcionarios):
    funcionarios_json = []
    for funcionario in funcionarios:
        funcionario = serializer_funcionario(funcionario)
        funcionarios_json.append(funcionario)
    return funcionarios_json