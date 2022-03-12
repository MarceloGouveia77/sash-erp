from django.urls import path
from rh import views

app_name = 'rh'

urlpatterns = [
    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('funcionarios/cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/editar/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/excluir/<int:funcionario_id>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('funcionarios/exportar/', views.exportar_funcionarios, name='exportar_funcionarios'),
    path('funcionarios/folha/', views.folha_pagamento, name='folha_pagamento'),
    path('funcionarios/folha/fechar/', views.fechar_folha_pagamento, name='fechar_folha_pagamento')
]