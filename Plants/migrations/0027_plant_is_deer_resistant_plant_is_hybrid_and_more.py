# Generated by Django 5.0.4 on 2024-04-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0026_plant_is_organic'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='is_deer_resistant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plant',
            name='is_hybrid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plant',
            name='is_rabbit_resistant',
            field=models.BooleanField(default=False),
        ),
    ]