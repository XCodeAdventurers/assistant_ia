# Generated by Django 4.2.13 on 2024-05-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_registrate',
            field=models.BooleanField(default=False),
        ),
    ]
