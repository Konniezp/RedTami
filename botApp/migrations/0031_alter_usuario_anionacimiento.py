# Generated by Django 5.0.1 on 2025-01-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0030_usuario_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='AnioNacimiento',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
    ]
