# Generated by Django 3.0.3 on 2020-06-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20200612_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
