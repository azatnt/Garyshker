# Generated by Django 3.0.3 on 2020-06-28 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0025_auto_20200627_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='slug',
        ),
    ]
