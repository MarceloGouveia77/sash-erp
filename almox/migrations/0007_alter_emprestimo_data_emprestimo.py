# Generated by Django 4.0.3 on 2022-03-31 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almox', '0006_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2022, 3, 31, 16, 7, 49, 212549), verbose_name='Data Empréstimo'),
        ),
    ]