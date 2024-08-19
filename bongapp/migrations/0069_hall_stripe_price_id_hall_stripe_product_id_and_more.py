# Generated by Django 5.0.2 on 2024-08-13 14:27

import datetime
import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongapp', '0068_alter_booking_day_alter_chatgroup_groupname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime(2024, 8, 13, 19, 57, 5, 438050)),
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
