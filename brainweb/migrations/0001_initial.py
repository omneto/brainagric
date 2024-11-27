# Generated by Django 5.1.2 on 2024-11-25 23:04

import brainweb.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Cultura')),
            ],
        ),
        migrations.CreateModel(
            name='RuralProducer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentId', models.CharField(max_length=14, unique=True, validators=[brainweb.models.validate_cpf_cnpj], verbose_name='CPF/CNPJ')),
                ('producerName', models.CharField(max_length=50, verbose_name='Nome do Produtor')),
                ('producerFarm', models.CharField(max_length=50, verbose_name='Nome da Fazenda')),
                ('city', models.CharField(max_length=60, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='Estado')),
                ('totalArea', models.DecimalField(decimal_places=2, default=0.0, max_digits=11, verbose_name='Área Total(ha)')),
                ('plantingArea', models.DecimalField(decimal_places=2, default=0.0, max_digits=11, verbose_name='Área Agricultável(ha)')),
                ('preservationArea', models.DecimalField(decimal_places=2, default=0.0, max_digits=11, verbose_name='Área Vegetação(ha)')),
                ('crops', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brainweb.crop')),
            ],
        ),
    ]