# Generated by Django 4.1.4 on 2022-12-26 20:04

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0010_sprzet_zdjecie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='data_utworzenia',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
        ),
    ]