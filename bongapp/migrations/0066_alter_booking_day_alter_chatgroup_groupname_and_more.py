# Generated by Django 5.0.2 on 2024-08-13 11:49

import datetime
import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongapp', '0065_hall_category_alter_booking_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime(2024, 8, 13, 17, 19, 52, 197768)),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='groupname',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hallbookings',
            name='booking_id',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, max_length=100, unique=True),
        ),
    ]
