# Generated by Django 5.0.1 on 2025-02-27 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0006_calculofrm_ruthash_respdetersalud_ruthash_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resptextofrm',
            old_name='altura_FRM5',
            new_name='altura_FRM4',
        ),
        migrations.RenameField(
            model_name='resptextofrm',
            old_name='peso_FRM6',
            new_name='peso_FRM5',
        ),
    ]
