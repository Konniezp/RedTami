# Generated by Django 5.0.1 on 2025-02-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0003_alter_usuario_rut_alter_usuario_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculofrm',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='respdetersalud',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resptextofrm',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='respusuariofactorriesgomod',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='respusuariofactorriesgonomod',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ultima_mamografia_anio',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuariorespuesta',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuariotextopregunta',
            name='Rut',
            field=models.CharField(max_length=255),
        ),
    ]
