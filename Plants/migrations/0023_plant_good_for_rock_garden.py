# Generated by Django 5.0.4 on 2024-04-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0022_plant_good_for_border'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='good_for_rock_garden',
            field=models.BooleanField(default=False),
        ),
    ]