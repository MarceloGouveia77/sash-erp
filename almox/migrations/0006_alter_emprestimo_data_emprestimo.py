# Generated by Django 4.0.3 on 2022-03-18 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almox', '0005_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 17, 18, 41, 184359), verbose_name='Data Empréstimo'),
        ),
    ]
