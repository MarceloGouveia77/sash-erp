# Generated by Django 4.0.3 on 2022-03-30 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_alter_contaspagar_data_alter_contasreceber_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 17, 9, 28, 205354), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='contasreceber',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 17, 9, 28, 205747), verbose_name='Data'),
        ),
    ]
