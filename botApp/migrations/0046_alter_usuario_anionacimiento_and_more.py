# Generated by Django 5.0.1 on 2025-02-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0045_alter_usuario_anionacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='AnioNacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
