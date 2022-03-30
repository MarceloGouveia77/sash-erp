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

TIPO_MOVIMENTACAO = [
    ('entrada', 'Entrada'),
    ('saida', 'Saída')
]

class ContasPagar(models.Model):
    compra = models.ForeignKey('compra.Compra', on_delete=models.CASCADE, null=True, blank=True)
    forma_pagamento = models.CharField('Forma Pagamento', choices=FORMAS_PAGAMENTO, default='avista', max_length=1024)
    descricao = models.CharField('Descrição', max_length=1024)
    data = models.DateTimeField('Data', default=datetime.datetime.today())
    pago = models.BooleanField('Pago', default=False)
    valor_total = models.FloatField('Valor Total')
    valor_pago = models.FloatField('Valor Pago')
    
    def obter_status(self):
        if self.pago:
            return '<span class="text-success fw-bold">Pago</span>'
        return '<span class="text-danger fw-bold">Pendente</span>'
    
    def obter_data(self):
        return self.data.strftime("%d/%m/%Y")
    
    def atualizar_conta(self, valor):
        self.valor_pago += valor
        if self.valor_pago >= self.valor_total:
            self.pago = True
        self.save()

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

    def obter_valor(self):
        return f'{self.valor:.2f}'
    
    def pagar_conta(self, data):
        self.conta.atualizar_conta(self.valor)
        self.pago = True
        self.save()
        
        ultima_mov = Movimentacao.objects.last()
        Movimentacao.objects.create(
            data=data,
            tipo='saida',
            saldo=(ultima_mov.saldo - self.valor),
            saldo_anterior=ultima_mov.saldo,
            pagamento=self
        )
    
    def __str__(self):
        return f'{self.obter_vencimento()} - {self.conta.descricao} - {self.descricao}'
    
class ContasReceber(models.Model):
    servico = models.ForeignKey('servico.Servico', on_delete=models.CASCADE, null=False)
    forma_pagamento = models.CharField('Forma Pagamento', choices=FORMAS_PAGAMENTO, default='avista', max_length=1024)
    descricao = models.CharField('Descrição', max_length=1024)
    data = models.DateTimeField('Data', default=datetime.datetime.today())
    recebido = models.BooleanField('Pago', default=False)
    valor_total = models.FloatField('Valor Total')
    valor_recebido = models.FloatField('Valor Pago')
    
    def obter_data(self):
        return self.data.strftime("%d/%m/%Y")
    
    def __str__(self):
        return f'{self.obter_data()} - {self.descricao}'
    
class Recebimentos(models.Model):
    conta = models.ForeignKey(ContasReceber, on_delete=models.CASCADE)
    vencimento = models.DateTimeField('Vencimento')
    descricao = models.CharField('Descrição', max_length=1024)
    valor = models.FloatField('Valor')
    recebido = models.BooleanField('Recebido', default=False)
    
    def obter_vencimento(self):
        return self.vencimento.strftime("%d/%m/%Y")
    
    def __str__(self):
        return f'{self.obter_vencimento()} - {self.conta.descricao} - {self.descricao}'
    
class Movimentacao(models.Model):
    data = models.DateTimeField('Data', auto_now=False, auto_now_add=False)
    tipo = models.CharField('Tipo', max_length=255, choices=TIPO_MOVIMENTACAO)
    saldo = models.FloatField('Saldo')
    saldo_anterior = models.FloatField('Saldo Anterior')
    recebimento = models.ForeignKey(Recebimentos, null=True, blank=True, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, null=True, blank=True, on_delete=models.CASCADE)
    
    def obter_descricao(self):
        if self.tipo == 'entrada' and self.recebimento:
            return f'{self.recebimento.conta.descricao} - {self.recebimento.descricao}'
        elif self.tipo == 'saida' and self.pagamento:
            return f'{self.pagamento.conta.descricao} - {self.pagamento.descricao}'
        else:
            return 'Correção de saldo'
    
    def obter_valor(self):
        return self.saldo - self.saldo_anterior