# Generated by Django 4.2.13 on 2024-05-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_person_is_registrate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='is_registrate',
            new_name='has_pay',
        ),
    ]
