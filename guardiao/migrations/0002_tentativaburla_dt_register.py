# Generated by Django 3.2.15 on 2023-12-29 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guardiao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tentativaburla',
            name='dt_register',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de Registro'),
            preserve_default=False,
        ),
    ]
