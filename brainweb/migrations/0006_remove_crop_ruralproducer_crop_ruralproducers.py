# Generated by Django 5.1.2 on 2024-11-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0005_auto_20241126_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='ruralProducer',
        ),
        migrations.AddField(
            model_name='crop',
            name='ruralProducers',
            field=models.ManyToManyField(null=True, to='brainweb.ruralproducer', verbose_name='Produtores'),
        ),
    ]
