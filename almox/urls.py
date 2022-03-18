from django.urls import path
from almox import views

app_name = 'almox'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/<int:item_id>/', views.detalhe, name='detalhe'),
    path('entradas/', views.entradas, name='entradas'),
    path('saidas/', views.saidas, name='saidas'),
    path('entradas/adicionar/', views.adicionar_entrada, name='adicionar_entrada'),
    path('cadastrar_item/', views.cadastrar_item, name='cadastrar_item'),
    path('editar_item/<int:item_id>', views.editar_item, name='editar_item'),
    path('item/deletar/<int:item_id>/', views.deletar_item, name='deletar_item'),
    path('entradas/deletar/<int:entrada_id>/', views.deletar_entrada, name='deletar_entrada'),
    path('saidas/adicionar/', views.adicionar_saida, name='adicionar_saida'),
    path('saidas/deletar/<int:saida_id>/', views.deletar_saida, name='deletar_saida'),
    path('recepcoes/', views.recepcao_compras, name='recepcao_compras'),
    path('recepcao/<int:compra_id>/', views.recepcao, name='recepcao'),
    path('recepcao/receber/item/', views.receber_item_compra, name='receber_item_compra')
]
