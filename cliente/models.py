from django.db import models

TIPO = [
    ('PF', 'Pessoa Física'),
    ('PJ', 'Pessoa Jurídica')
]
    
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    tipo = models.CharField('Tipo', max_length=1024, choices=TIPO)
    cpf = models.CharField('CPF', max_length=1024, null=True, blank=True, unique=True)
    cnpj = models.CharField('CNPJ', max_length=1024, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.nome
