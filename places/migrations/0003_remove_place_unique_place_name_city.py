# Generated by Django 4.2.7 on 2023-12-05 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_place_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='place',
            name='unique_place_name_city',
        ),
    ]
