# Generated by Django 5.0.1 on 2025-01-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0029_rename_mitabla_mensajecontenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
