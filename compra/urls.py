from django.urls import path
from compra import views

app_name='compra'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('editar/<int:compra_id>/', views.editar, name='editar'),
    path('adicionar/item/', views.adicionar_item_compra, name='adicionar_item_compra')
]