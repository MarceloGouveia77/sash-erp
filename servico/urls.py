from django.urls import path
from servico import views

app_name = 'servico'

urlpatterns = [
    path('', views.index, name='index'),
    path('os/<int:os_id>/', views.detalhe_os, name='detalhe_os'),
    path('os/', views.os, name='os'),
    path('cadastrar',views.cadastrar, name='cadastrar'),
    path('editar/<int:servico_id>', views.editar, name='editar'),
    path('deletar/<int:servico_id>/', views.deletar, name='deletar'),
    
]