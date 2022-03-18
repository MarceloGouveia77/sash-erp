from django.db import models
from rh.models import Departamento, Funcionario

# Create your models here.

FORMAS_PAGAMENTO = [
    ('avista', 'À Vista'),
    ('1x', 'Parcelado em 1x'),
    ('2x', 'Parcelado em 2x'),
    ('3x', 'Parcelado em 3x'),
    ('4x', 'Parcelado em 4x'),
    ('5x', 'Parcelado em 5x'),
    ('6x', 'Parcelado em 6x'),
    ('7x', 'Parcelado em 7x'),
    ('8x', 'Parcelado em 8x'),
    ('9x', 'Parcelado em 9x'),
    ('10x', 'Parcelado em 10x'),
    ('11x', 'Parcelado em 11x'),
    ('12x', 'Parcelado em 12x'),
]

class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    cnpj = models.CharField('CNPJ', max_length=50, unique=True)

    def __str__(self):
        return self.nome
    
class Compra(models.Model):
    solicitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data = models.DateTimeField('Data', auto_now_add=True)
    centro_custo = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=50, choices=FORMAS_PAGAMENTO, default='avista')
    pago = models.BooleanField('Pago', default=False)
    entregue = models.BooleanField('Entregue', default=False)
    valor_total = models.FloatField('Valor Total', default=0)
    descricao = models.CharField('Descrição', max_length=1024)
    
    def recalcular_valor_total(self):
        compra_itens = CompraItem.objects.filter(compra=self)
        valor_total = 0
        for compra in compra_itens:
            valor_total += compra.valor_total
        self.valor_total = valor_total
        self.save()
    
    
class CompraItem(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    item = models.ForeignKey('almox.Item', on_delete=models.CASCADE)
    valor = models.FloatField('Valor')
    valor_total = models.FloatField('Valor', default=0)
    quantidade = models.FloatField('Quantidade')
    estoque = models.BooleanField('Estoque', default=True)
    recebido = models.BooleanField('Recebido', default=False)
    
    def obter_subtotal(self):
        return self.valor * self.quantidade
    
    def alterar_quantidade(self, qtd):
        self.quantidade += qtd
        self.save()
    
    def save(self, *args, **kwargs):
        if self.valor:
            self.item.valor = self.valor
            self.item.save()
        self.valor_total = self.obter_subtotal()
        super().save(*args, **kwargs)
        self.compra.recalcular_valor_total()