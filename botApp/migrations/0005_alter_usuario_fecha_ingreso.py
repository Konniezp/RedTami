# Generated by Django 5.0.1 on 2024-01-15 14:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0004_rename_texto_pregunta_pregunta_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Fecha_Ingreso',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
