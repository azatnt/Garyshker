# Generated by Django 3.0.3 on 2020-06-22 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Obrazovanie', '0019_report_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Obrazovanie.Genre'),
        ),
    ]
