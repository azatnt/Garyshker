# Generated by Django 3.0.3 on 2020-06-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0010_auto_20200620_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='item-image'),
        ),
    ]
