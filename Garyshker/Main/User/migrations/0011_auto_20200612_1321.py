# Generated by Django 3.0.3 on 2020-06-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
