# Generated by Django 5.0.4 on 2024-04-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0018_plant_heat_tolerant'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='pollinator_friendly',
            field=models.BooleanField(default=False),
        ),
    ]