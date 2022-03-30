from django.db import models
from cliente.models import Cliente
# Create your models here.

class Servico(models.Model):
    descricao = models.CharField('Descrição', max_length=1024)
    valor = models.FloatField('Valor', default=0)
    

    def __str__(self) -> str:
        return self.descricao
    
class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField('Data', auto_now_add=True)
    valor = models.FloatField('Valor', default=0)
    descricao = models.CharField('Descricao', max_length=255)
    pago = models.BooleanField('Pago', default=False)
    conclusao = models.DateField('Conclusão', auto_now=False, auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.descricao
    
class ServicosOS(models.Model):
    os = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    quantidade = models.FloatField('Quantidade', default=1)
    
    def obter_valor(self):
        return self.servico.valor * self.quantidade