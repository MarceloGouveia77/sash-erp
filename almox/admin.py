from django.contrib import admin
from almox.models import Categoria, Item, Entrada, EntradaItem, Saida, SaidaItem, Emprestimo
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Item)
admin.site.register(Entrada)
admin.site.register(EntradaItem)
admin.site.register(Saida)
admin.site.register(SaidaItem)
admin.site.register(Emprestimo)
