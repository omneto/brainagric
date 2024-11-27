# Generated by Django 5.1.2 on 2024-11-26 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0002_alter_ruralproducer_crops'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruralproducer',
            name='crops',
        ),
        migrations.AddField(
            model_name='crop',
            name='ruralProducer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='brainweb.ruralproducer', verbose_name='Culturas'),
            preserve_default=False,
        ),
    ]