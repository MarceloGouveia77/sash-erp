from django.contrib import admin
from compra.models import Fornecedor, Compra, CompraItem
# Register your models here.

admin.site.register(Fornecedor)
admin.site.register(Compra)
admin.site.register(CompraItem)