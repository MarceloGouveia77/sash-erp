from django.contrib import admin
from servico.models import Servico, OrdemServico, ServicosOS
# Register your models here.

admin.site.register(Servico)
admin.site.register(OrdemServico)
admin.site.register(ServicosOS)