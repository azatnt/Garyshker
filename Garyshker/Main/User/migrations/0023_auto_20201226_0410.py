# Generated by Django 3.0.3 on 2020-12-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0022_auto_20200711_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='garysh.jpg', upload_to='user-profile-image', verbose_name=''),
        ),
    ]
