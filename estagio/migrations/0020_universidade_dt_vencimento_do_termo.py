# Generated by Django 3.2.15 on 2023-06-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0019_responsavel_universidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidade',
            name='dt_vencimento_do_termo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
