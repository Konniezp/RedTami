# Generated by Django 5.0.1 on 2025-02-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0037_pregdetersalud_pregfactorriesgonomod_opcdetersalud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='respusuariofactorriesgonomod',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
