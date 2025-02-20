# Generated by Django 5.0.1 on 2025-02-20 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajecontenido',
            name='opcresTM',
        ),
        migrations.RemoveField(
            model_name='mensajecontenido',
            name='opcresUS',
        ),
        migrations.RemoveField(
            model_name='mensajecontenido',
            name='opcrespDS',
        ),
        migrations.RemoveField(
            model_name='mensajecontenido',
            name='opcrespFRM',
        ),
        migrations.RemoveField(
            model_name='mensajecontenido',
            name='opcrespFRNM',
        ),
        migrations.CreateModel(
            name='filtro_mensaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID filtro mensaje')),
                ('mensaje_contenido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.mensajecontenido')),
                ('opcresTM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.usuariorespuesta')),
                ('opcresUS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.usuario')),
                ('opcrespDS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.respdetersalud')),
                ('opcrespFRM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.respusuariofactorriesgomod')),
                ('opcrespFRNM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.respusuariofactorriesgonomod')),
            ],
        ),
    ]
