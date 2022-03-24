from django.urls import path
from compra import views

app_name='compra'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('concluir/', views.concluir_compra, name='concluir_compra'),
    path('editar/<int:compra_id>/', views.editar, name='editar'),
    path('adicionar/item/', views.adicionar_item_compra, name='adicionar_item_compra'),
    path('item/alterar/quantidade/', views.alterar_quantidade_item_compra, name='alterar_quantidade_item_compra'),
    path('item/remover/<int:compra_item_id>/', views.remover_item_compra, name='remover_item_compra'),
]