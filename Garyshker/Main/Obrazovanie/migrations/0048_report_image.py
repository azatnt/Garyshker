# Generated by Django 3.0.3 on 2020-09-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0047_report_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, upload_to='item-image'),
        ),
    ]