# Generated by Django 5.0.4 on 2024-04-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0019_plant_pollinator_friendly'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='attracts_butterflies',
            field=models.BooleanField(default=False),
        ),
    ]
