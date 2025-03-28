# Generated by Django 5.0.1 on 2025-02-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0005_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculofrm',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respdetersalud',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='resptextofrm',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respusuariofactorriesgomod',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respusuariofactorriesgonomod',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ultima_mamografia_anio',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuariorespuesta',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuariotextopregunta',
            name='RutHash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
