# Generated by Django 4.0.3 on 2022-03-31 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_alter_contaspagar_data_alter_contasreceber_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 16, 7, 49, 208771), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='contasreceber',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 16, 7, 49, 209159), verbose_name='Data'),
        ),
    ]
