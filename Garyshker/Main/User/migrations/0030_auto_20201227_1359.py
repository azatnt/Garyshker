# Generated by Django 3.0.3 on 2020-12-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0029_auto_20201227_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, default='garysh.jpg', upload_to='user-profile-images'),
        ),
    ]
