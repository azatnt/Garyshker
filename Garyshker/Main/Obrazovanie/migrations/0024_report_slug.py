# Generated by Django 3.0.3 on 2020-06-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0023_auto_20200626_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
