from django.db import models
from cliente.models import Cliente
# Create your models here.

class TipoServico(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    valor = models.FloatField('Valor')
    
    def __str__(self) -> str:
        return self.nome

class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=1024)
    valor = models.FloatField('Valor', default=0)
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    data_conclusao = models.DateField('Data Conclusão')
    concluido = models.BooleanField('Concluído', default=False)
    
    def obter_data_inicio(self):
        if self.data:
            return self.data.strftime("%d/%m/%Y")
        return ''
    
    def obter_data_conclusao(self):
        if self.data_conclusao:
            return self.data_conclusao.strftime("%d/%m/%Y")
        return ''
    
    def __str__(self) -> str:
        return self.descricao
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.valor = self.tipo.valor
        super().save(*args, **kwargs)
        
    