# Generated by Django 3.0.3 on 2020-06-24 19:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Obrazovanie', '0020_report_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]