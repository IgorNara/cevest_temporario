# Generated by Django 3.2.15 on 2023-06-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0020_universidade_dt_vencimento_do_termo'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='mensagem',
            field=models.CharField(max_length=80, null=True, verbose_name='Mensagem'),
        ),
    ]
