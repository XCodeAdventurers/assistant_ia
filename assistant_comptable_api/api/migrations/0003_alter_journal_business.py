# Generated by Django 5.0.5 on 2024-05-07 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_journal_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.business'),
        ),
    ]