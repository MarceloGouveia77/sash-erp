from django.db import models
from rh.models import Funcionario
from servico.models import Servico
import datetime
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=255, null=False)

    def __str__(self):
        return (self.nome)
        
class Item(models.Model):
    nome = models.CharField("Nome", max_length=255, null=False)
    quantidade = models.IntegerField("QTD", default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.FloatField("Valor", default=0)
    
    def __str__(self):
        return (self.nome)
    
    def saida_item(self, quantidade):
        self.quantidade -= quantidade
        self.save()
    
    def entrada_item(self, quantidade):
        self.quantidade += quantidade
        self.save()

class Entrada(models.Model):
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, null=True, blank=True, on_delete=models.CASCADE)
    valor_total = models.FloatField('Valor Total')
    
    def calcular_valor_total(self):
        entradas = EntradaItem.objects.filter(entrada_id = self.id)
        valor_total = 0 
        for entrada in entradas:
            valor_total += entrada.valor
        return valor_total
    
    def save(self, *args, **kwargs):
        self.valor_total = self.calcular_valor_total()
        super().save(*args, **kwargs)
    
class EntradaItem(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.FloatField('Quantidade', default=1)    
    valor = models.FloatField('Valor')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.valor = self.item.valor
        super().save(*args, **kwargs)
    
class Saida(models.Model):
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, null=True, blank=True, on_delete=models.CASCADE)
    valor_total = models.FloatField('Valor Total')
    
    def calcular_valor_total(self):
        saidas = SaidaItem.objects.filter(saida_id = self.id)
        valor_total = 0 
        for saida in saidas:
            valor_total += saida.valor
        return valor_total
    
    def save(self, *args, **kwargs):
        self.valor_total = self.calcular_valor_total()
        super().save(*args, **kwargs)
    
    
class SaidaItem(models.Model):
    saida = models.ForeignKey(Saida, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.FloatField('Quantidade', default=1) 
    valor = models.FloatField('Valor')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.valor = self.item.valor
        super().save(*args, **kwargs)
    
class Emprestimo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    quantidade = models.IntegerField('Quantidade', default=0)
    data_emprestimo = models.DateField('Data Empréstimo', default=datetime.datetime.today())
    data_devolucao = models.DateField('Devolução', null=True, blank=True)
    devolvido = models.BooleanField('Foi Devolvido', default=False)

    def __str__(self):
        return f'{self.funcionario} - {self.item}'
    
    def obter_data_emprestimo(self):
        return self.data_emprestimo.strftime('%d/%m/%Y')
    
    def obter_data_devolucao(self):
        if self.data_devolucao:
            return self.data_devolucao.strftime('%d/%m/%Y')
        return ''
    
    def verificar_disponibilidade(self):
        if self.quantidade <= self.item.quantidade:
            return True
        return False