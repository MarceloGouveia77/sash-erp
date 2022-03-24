import datetime
from django.db import models


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

class ContasPagar(models.Model):
    compra = models.ForeignKey('compra.Compra', on_delete=models.CASCADE, null=True, blank=True)
    forma_pagamento = models.CharField('Forma Pagamento', choices=FORMAS_PAGAMENTO, default='avista', max_length=1024)
    descricao = models.CharField('Descrição', max_length=1024)
    data = models.DateTimeField('Data', default=datetime.datetime.today())
    pago = models.BooleanField('Pago', default=False)
    valor_total = models.FloatField('Valor Total')
    valor_pago = models.FloatField('Valor Pago')
    
    def obter_data(self):
        return self.data.strftime("%d/%m/%Y")

    def __str__(self):
        return f'{self.obter_data()} - {self.descricao}'
    
class Pagamentos(models.Model):
    conta = models.ForeignKey(ContasPagar, on_delete=models.CASCADE)
    vencimento = models.DateTimeField('Vencimento')
    descricao = models.CharField('Descrição', max_length=1024)
    valor = models.FloatField('Valor')
    pago = models.BooleanField('Pago', default=False)
    
    def obter_vencimento(self):
        return self.vencimento.strftime("%d/%m/%Y")
    
    def __str__(self):
        return f'{self.obter_vencimento()} - {self.conta.descricao} - {self.descricao}'