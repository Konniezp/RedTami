# Generated by Django 5.0.1 on 2025-02-19 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0049_resptextofrm_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultima_mamografia_anio',
            name='id_usuario',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='botApp.usuario'),
            preserve_default=False,
        ),
    ]
