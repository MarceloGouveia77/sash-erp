from django.urls import path
from financeiro import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.index, name='index')
]
