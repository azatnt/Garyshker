# Generated by Django 3.0.3 on 2020-06-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0012_remove_item_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Obrazovanie.Genre'),
        ),
    ]