# Generated by Django 5.0.1 on 2025-02-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0004_alter_calculofrm_rut_alter_respdetersalud_rut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
