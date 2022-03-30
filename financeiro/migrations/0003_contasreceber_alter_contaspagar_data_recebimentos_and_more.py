# Generated by Django 4.0.3 on 2022-03-24 19:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_alter_servico_valor'),
        ('financeiro', '0002_alter_contaspagar_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContasReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pagamento', models.CharField(choices=[('avista', 'À Vista'), ('1x', 'Parcelado em 1x'), ('2x', 'Parcelado em 2x'), ('3x', 'Parcelado em 3x'), ('4x', 'Parcelado em 4x'), ('5x', 'Parcelado em 5x'), ('6x', 'Parcelado em 6x'), ('7x', 'Parcelado em 7x'), ('8x', 'Parcelado em 8x'), ('9x', 'Parcelado em 9x'), ('10x', 'Parcelado em 10x'), ('11x', 'Parcelado em 11x'), ('12x', 'Parcelado em 12x')], default='avista', max_length=1024, verbose_name='Forma Pagamento')),
                ('descricao', models.CharField(max_length=1024, verbose_name='Descrição')),
                ('data', models.DateTimeField(default=datetime.datetime(2022, 3, 24, 16, 25, 28, 272206), verbose_name='Data')),
                ('recebido', models.BooleanField(default=False, verbose_name='Pago')),
                ('valor_total', models.FloatField(verbose_name='Valor Total')),
                ('valor_recebido', models.FloatField(verbose_name='Valor Pago')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servico.servico')),
            ],
        ),
        migrations.AlterField(
            model_name='contaspagar',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 24, 16, 25, 28, 270849), verbose_name='Data'),
        ),
        migrations.CreateModel(
            name='Recebimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vencimento', models.DateTimeField(verbose_name='Vencimento')),
                ('descricao', models.CharField(max_length=1024, verbose_name='Descrição')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('recebido', models.BooleanField(default=False, verbose_name='Recebido')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.contasreceber')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=255, verbose_name='Tipo')),
                ('saldo', models.FloatField(verbose_name='Saldo')),
                ('saldo_anterior', models.FloatField(verbose_name='Saldo Anterior')),
                ('pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeiro.pagamentos')),
                ('recebimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeiro.recebimentos')),
            ],
        ),
    ]
