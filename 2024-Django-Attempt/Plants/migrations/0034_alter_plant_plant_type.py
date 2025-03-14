# Generated by Django 5.0.4 on 2024-04-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0033_plant_is_waterwise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('an', 'Annual'), ('bi', 'Biennial'), ('pe', 'Perennial'), ('tp', 'Tender Perennial'), ('sh', 'Shrub'), ('tr', 'Tree'), ('vi', 'Vine'), ('un', 'Unknown')], default='pe', max_length=2),
        ),
    ]
