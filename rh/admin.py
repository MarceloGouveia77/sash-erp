from django.contrib import admin
from rh.models import Departamento, Funcionario, HoraExtra, Falta, Funcao, FolhaPagamento
# Register your models here.


admin.site.register(FolhaPagamento)
admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(HoraExtra)
admin.site.register(Falta)
admin.site.register(Funcao)