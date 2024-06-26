# Generated by Django 5.0.4 on 2024-04-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0003_alter_plantlink_options_remove_plant_resources_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='exposure',
            field=models.CharField(choices=[('fs', 'Full Sun (6+)'), ('pu', 'Partial Sun (morning, 4-6H)'), ('pd', 'Partial Shade (morning, <=4H)'), ('sh', 'Shade')], default='fs', max_length=2),
        ),
    ]
