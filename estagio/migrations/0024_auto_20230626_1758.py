# Generated by Django 3.2.15 on 2023-06-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0023_auto_20230626_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='nome',
            field=models.CharField(default='', max_length=50, verbose_name='Nome vagas'),
            preserve_default=False,
        ),
    ]
