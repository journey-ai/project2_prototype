# Generated by Django 4.0.3 on 2023-01-26 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_station_search_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station_search',
            name='create_date',
        ),
    ]
