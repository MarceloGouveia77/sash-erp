# Generated by Django 4.0.3 on 2022-03-30 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almox', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2022, 3, 30, 17, 8, 58, 66127), verbose_name='Data Empréstimo'),
        ),
    ]
