# Generated by Django 4.0.3 on 2022-03-31 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='token'),
        ),
    ]