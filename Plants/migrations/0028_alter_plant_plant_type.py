# Generated by Django 5.0.4 on 2024-04-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0027_plant_is_deer_resistant_plant_is_hybrid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('an', 'Annual'), ('bi', 'Biennial'), ('pe', 'Perennial'), ('tp', 'Tender Perennial'), ('sh', 'Shrub'), ('tr', 'Tree'), ('vi', 'Vine')], default='pe', max_length=2),
        ),
    ]