# Generated by Django 4.0.3 on 2022-03-18 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almox', '0008_entradaitem_compra_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 17, 23, 21, 706339), verbose_name='Data Empréstimo'),
        ),
    ]
