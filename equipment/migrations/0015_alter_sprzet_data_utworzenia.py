# Generated by Django 4.1.4 on 2022-12-30 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0014_alter_sprzet_data_utworzenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='data_utworzenia',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
