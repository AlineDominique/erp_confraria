# Generated by Django 3.2.8 on 2021-12-10 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data', models.DateField(verbose_name='Data')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produto.categoria')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='DoacaoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recebido', models.BooleanField(default=False)),
                ('data_entrega', models.DateTimeField(blank=True, null=True, verbose_name='Data de entrega')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evento.evento')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoa.pessoa')),
            ],
            options={
                'verbose_name': 'Doação de Evento',
                'verbose_name_plural': 'Doações de Eventos',
                'unique_together': {('pessoa', 'evento')},
            },
        ),
    ]
