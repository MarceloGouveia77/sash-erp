from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_sistema, name='login_sistema'),
    path('logout', views.logout_sistema, name='logout_sistema')
]