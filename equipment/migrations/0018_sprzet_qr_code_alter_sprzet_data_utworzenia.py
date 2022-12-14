# Generated by Django 4.1.4 on 2022-12-30 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0017_alter_sprzet_data_utworzenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprzet',
            name='QR_code',
            field=models.ImageField(blank=True, upload_to='QR_code'),
        ),
        migrations.AlterField(
            model_name='sprzet',
            name='data_utworzenia',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
