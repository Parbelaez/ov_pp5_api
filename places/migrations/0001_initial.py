# Generated by Django 4.2.7 on 2023-12-05 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('place_name', models.CharField(max_length=100)),
                ('place_type', models.CharField(choices=[('restaurant', 'Restaurant'), ('bar', 'Bar'), ('cafe', 'Cafe'), ('hotel', 'Hotel'), ('museum', 'Museum'), ('park', 'Park'), ('beach', 'Beach'), ('other', 'Other')], default='other', max_length=32)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_place_zlhcpb', upload_to='positive/place_pictures/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('city', 'place_name')},
            },
        ),
    ]
