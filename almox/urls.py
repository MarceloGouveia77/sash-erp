from django.urls import path
from almox import views

app_name = 'almox'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/<int:item_id>/', views.detalhe, name='detalhe')
]
