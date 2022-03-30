from django.urls import path
from financeiro import views

app_name = 'financeiro'

urlpatterns = [
    path('movimentacoes', views.movimentacoes, name='movimentacoes'),
    path('contas/', views.contas_pagar, name='contas_pagar'),
    path('contas/pagar/<str:pagina>/', views.pagar, name='pagar'),
    path('contas/pagamentos/pagar/', views.pagar_conta, name='pagar_conta'),
    
    # API / JSON
    path('json/conta/pagamentos/<int:conta_id>/', views.obter_pagamentos_conta, name='obter_pagamentos_conta')
]
