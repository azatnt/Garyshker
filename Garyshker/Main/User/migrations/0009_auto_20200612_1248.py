# Generated by Django 3.0.3 on 2020-06-12 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_delete_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]