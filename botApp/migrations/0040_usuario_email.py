# Generated by Django 5.0.1 on 2025-02-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0039_remove_respusuariofactorriesgonomod_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
