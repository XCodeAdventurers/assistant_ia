# Generated by Django 4.2.11 on 2024-05-07 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_business_country_alter_business_district_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='description',
            new_name='libelle',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='business',
        ),
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.person'),
        ),
    ]
