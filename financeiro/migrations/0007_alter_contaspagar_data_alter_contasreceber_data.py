# Generated by Django 4.0.3 on 2022-03-29 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0006_alter_contaspagar_data_alter_contasreceber_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 15, 46, 33, 397149), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='contasreceber',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 15, 46, 33, 398392), verbose_name='Data'),
        ),
    ]
