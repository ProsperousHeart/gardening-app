# Generated by Django 5.0.4 on 2024-04-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0032_plant_is_good_for_shrubs'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='is_waterwise',
            field=models.BooleanField(default=False),
        ),
    ]