# Generated by Django 5.0.1 on 2024-01-15 14:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0005_alter_usuario_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Fecha_Ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]