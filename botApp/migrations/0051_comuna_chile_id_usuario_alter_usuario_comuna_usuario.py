# Generated by Django 5.0.1 on 2025-02-19 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0050_alter_ultima_mamografia_anio_id_usuario'),
    ]

    operations = [
        #migrations.AddField(
            #model_name='comuna_chile',
            #name='id_usuario',
            #field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='botApp.usuario'),
            #preserve_default=False,
        #),
        migrations.AlterField(
            model_name='usuario',
            name='Comuna_Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.comuna_chile'),
        ),
    ]
