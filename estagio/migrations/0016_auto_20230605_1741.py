# Generated by Django 3.2.15 on 2023-06-05 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0015_auto_20230602_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante_vaga',
            name='local_do_estagio_de_pretensao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pretensao', to='estagio.locais_de_estagio'),
        ),
        migrations.AddField(
            model_name='historico_processo',
            name='status',
            field=models.CharField(choices=[('0', 'Aguardando documentação do aluno'), ('1', 'Aguardando liberação de vaga'), ('2', 'Aguardando termo assinado pela universidade')], default=0, max_length=1, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='processo',
            name='data_inclusao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='processo',
            name='status',
            field=models.CharField(choices=[('0', 'Aguardando documentação do aluno'), ('1', 'Aguardando liberação da univerdade'), ('2', 'Aguardando liberação de vaga'), ('3', 'Aguardando termo assinado pela universidade'), ('4', 'Processo de seleção concluída'), ('5', 'Estágio concluído')], default=0, max_length=1, verbose_name='Status'),
        ),
    ]
