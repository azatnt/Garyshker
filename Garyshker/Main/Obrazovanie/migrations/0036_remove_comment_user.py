# Generated by Django 3.0.3 on 2020-07-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0035_auto_20200717_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
