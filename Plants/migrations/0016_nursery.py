# Generated by Django 5.0.4 on 2024-04-24 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0015_plant_drought_tolerant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
                ('plants', models.ManyToManyField(blank=True, to='Plants.plant')),
            ],
        ),
    ]
