# Generated by Django 5.0.1 on 2025-01-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0031_alter_usuario_anionacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ultima_mamografia_anio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de última mamografía')),
                ('Rut', models.CharField(max_length=10)),
                ('anio_ult_mamografia', models.DateField(verbose_name='Año de última mamografía')),
                ('tiempo_transc_ult_mamografia', models.CharField(max_length=4, verbose_name='Tiempo transcurrido')),
            ],
        ),
    ]
