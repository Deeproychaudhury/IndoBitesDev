# Generated by Django 5.0.2 on 2024-08-12 06:46

import datetime
import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongapp', '0055_chatgroup_banlist_alter_booking_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('ammenity', models.CharField(choices=[('Wifi', 'Wifi'), ('Parking', 'Parking'), ('Air Conditioning', 'Air Conditioning'), ('Stage', 'Stage')], default='', max_length=100)),
                ('hallcapacity', models.CharField(choices=[('2', '2'), ('4', '4'), ('10', '10'), ('buffet', 'buffet')], default='2', max_length=100)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime(2024, 8, 12, 12, 16, 45, 393534)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seats',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('10', '10'), ('buffet', 'buffet')], default='2', max_length=100),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='groupname',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, max_length=100, unique=True),
        ),
    ]
