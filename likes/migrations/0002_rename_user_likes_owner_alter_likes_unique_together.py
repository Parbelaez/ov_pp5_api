# Generated by Django 4.2.7 on 2023-12-06 16:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_post_place'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('owner', 'post')},
        ),
    ]
