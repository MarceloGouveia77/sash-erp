from django.urls import path
from api.controllers import core, users, rh, cliente, compra

app_name='api'

urlpatterns = [
    path('core/auth', core.auth, name='core_auth'),
    path('core/logout', core.logout, name='core_logout'),
    
    path('users/me', users.me, name='users_me'),
    path('users/', users.obter_usuarios, name='obter_usuarios'),
    
    path('rh/funcionarios/', rh.funcionarios, name='funcionarios'),
    path('rh/funcionarios/<int:pk>/', rh.funcionarios, name='funcionarios'),
    path('rh/departamentos/', rh.departamentos, name='departamentos'),
    path('rh/departamentos/<int:pk>/', rh.departamentos, name='departamentos'),
    path('rh/funcoes/', rh.funcoes, name='funcoes'),
    path('rh/funcoes/<int:pk>/', rh.funcoes, name='funcoes'),
    
    path('clientes/', cliente.clientes, name='clientes'),
    path('clientes/<int:pk>/', cliente.clientes, name='clientes'),
    
    
    path('compras/', compra.compras, name='compras'),
    path('compras/<int:pk>/', compra.compras, name='compras'),
    path('compras/items/', compra.compra_items, name='compra_items'),
    path('compras/items/<int:pk>/', compra.compra_items, name='compra_items'),
    path('compras/fornecedores/', compra.fornecedores, name='fornecedores'),
    path('compras/fornecedores/<int:pk>/', compra.fornecedores, name='fornecedores'),
]

