# Generated by Django 4.2.13 on 2024-05-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_budget_etat_budget_cloturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('revenue', 'Revenue'), ('expense', 'Dépense')], max_length=20),
        ),
    ]
