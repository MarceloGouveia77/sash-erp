from django.db import models
import datetime

ESTADOS = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    
    def __str__(self):
        return self.nome

class Funcao(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    salario_base = models.FloatField('Salário Base', default=0)
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=1024)
    cpf = models.CharField('CPF', max_length=50, null=False, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=True)
    data_admissao = models.DateField('Data Admissão', auto_now=False, auto_now_add=False)
    data_demissao = models.DateField('Data Demissão', auto_now=False, auto_now_add=False, null=True, blank=True)
    email = models.EmailField('Email', max_length=254)
    ativo = models.BooleanField('Ativo', default=True)
    celular = models.CharField('Celular', max_length=50)
    
    endereco_rua = models.CharField('Rua', max_length=255)
    endereco_numero = models.CharField('Numero', max_length=50)
    endereco_bairro = models.CharField('Bairro', max_length=50)
    endereco_complemento = models.CharField('Complemento', max_length=50, null=True, blank=True)
    endereco_cep = models.CharField('CEP', max_length=50)
    endereco_cidade = models.CharField('Cidade', max_length=50)
    endereco_estado = models.CharField('Estado', choices=ESTADOS, default='GO', max_length=50)
    
    salario = models.FloatField('Salário', default=0)
    valor_diaria = models.FloatField('Diária', default=0)
    
    def __str__(self):
        return f'{self.nome} - {self.departamento}'
    
    def obter_data_admissao(self):
        if self.data_admissao:
            return self.data_admissao.strftime("%d/%m/%Y")
        return ''
    
    def obter_data_demissao(self):
        if self.data_demissao:
            return self.data_demissao.strftime("%d/%m/%Y")
        return ''
    
    def obter_valor_dia(self):
        return self.salario / 30
    
    def obter_valor_hora(self):
        return (self.obter_valor_dia() / 8)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.salario = self.funcao.salario_base
        super().save(*args, **kwargs)
        
class Falta(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    justificada = models.BooleanField('Justificada', default=False)
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    motivo = models.CharField('Motivo', max_length=1024, null=True, blank=True)
    valor = models.FloatField('Valor', default=0)
    
    def __str__(self):
        return f'{self.funcionario} - {self.data.strftime("%d/%m/%Y")}'
    
    def obter_data(self):
        return self.data.strftime("%d/%m")
    
    def save(self, *args, **kwargs):
        if not self.id and not self.justificada:
            self.valor = (self.funcionario.obter_valor_dia())
        if self.justificada:
            self.valor = 0
        super().save(*args, **kwargs)
    
class HoraExtra(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    entrada = models.DateTimeField('Entrada', auto_now=False, auto_now_add=False)
    saida = models.DateTimeField('Saida', auto_now=False, auto_now_add=False)
    tempo_total = models.IntegerField('Tempo Total', default=0)
    valor = models.FloatField('Valor', default=0)
    
    def __str__(self):
        return f'{self.funcionario} - {self.obter_tempo_total()}'
    
    def obter_data(self):
        return self.entrada.strftime("%d/%m")
    
    def obter_tempo_total(self):
        horas = int(self.tempo_total / 60)
        minutos = self.tempo_total % 60
        return f'{horas:02}:{minutos:02}'
        
    
    def save(self, *args, **kwargs):
        segundos = (self.saida - self.entrada).seconds
        self.tempo_total = (segundos / 60)
        
        if not self.id:
            self.valor = ((self.funcionario.obter_valor_hora() / 60) * self.tempo_total)
        
        super().save(*args, **kwargs)
        
class Diaria(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    dia = models.DateField('Dia', auto_now=False, auto_now_add=False)
    valor = models.FloatField('Valor', default=0)
    
    def __str__(self):
        return f'{self.funcionario} - {self.dia.strftime("%d/%m/%Y")}'
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.valor = self.funcionario.valor_diaria
        super().save(*args, **kwargs)
        
class FolhaPagamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    mes = models.DateField('Mes', auto_now=False, auto_now_add=False)
    fechada = models.BooleanField('Fechada', default=False)
    
    salario_base = models.FloatField('Salário Base', default=0)
    horas_extra = models.FloatField('Horas Extra', default=0)
    faltas = models.FloatField('Faltas', default=0)
    descontos = models.FloatField('Descontos', default=0)
    total = models.FloatField('Total', default=0)
    
    def __str__(self):
        return f'{self.funcionario} - {self.mes.strftime("%B/%Y")}'

    def calcular_faltas(self):
        faltas = Falta.objects.filter(
            funcionario=self.funcionario,
            data__month=self.mes.month, 
            data__year=self.mes.year
        )
        valor_faltas = 0
        for falta in faltas:
            valor_faltas += falta.valor
        return {
            'qtd': faltas.count(),
            'valor': valor_faltas,
            'faltas': faltas
        }
    
    def calcular_horas_extras(self):
        horas_extras = HoraExtra.objects.filter(
            funcionario=self.funcionario,
            entrada__month=self.mes.month,
            entrada__year=self.mes.year
        )
        valor_horas = 0
        for hora in horas_extras:
            valor_horas += hora.valor
        return {
            'qtd': horas_extras.count(),
            'valor': valor_horas,
            'horas': horas_extras
        }
    
    def calcular_salario_base(self):
        return self.funcionario.salario
    
    def save(self, *args, **kwargs):
        self.horas_extra = self.calcular_horas_extras()['valor']
        self.salario_base = self.calcular_salario_base()
        self.faltas = self.calcular_faltas()['valor']
        
        self.total = (self.salario_base + self.horas_extra) - (self.descontos + self.faltas)
        
        super().save(*args, **kwargs)