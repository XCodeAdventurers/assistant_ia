# Generated by Django 4.2.11 on 2024-05-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_account_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialgoal',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
