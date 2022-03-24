from django.contrib import admin
from financeiro.models import Pagamentos, ContasPagar
# Register your models here.

admin.site.register(ContasPagar)
admin.site.register(Pagamentos)