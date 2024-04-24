# Generated by Django 5.0.4 on 2024-04-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0012_alter_plantlink_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantlink',
            name='type',
            field=models.CharField(choices=[('aa', 'Academic Article'), ('bl', 'Blog'), ('bk', 'Book'), ('mg', 'Master Gardener'), ('nu', 'Nursery Information'), ('ot', 'Other'), ('yt', 'YouTube')], max_length=2),
        ),
    ]