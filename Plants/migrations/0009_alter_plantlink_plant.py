# Generated by Django 5.0.4 on 2024-04-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0008_alter_plant_hardiness_zone_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantlink',
            name='plant',
            field=models.ManyToManyField(blank=True, related_name='links', to='Plants.plant'),
        ),
    ]
