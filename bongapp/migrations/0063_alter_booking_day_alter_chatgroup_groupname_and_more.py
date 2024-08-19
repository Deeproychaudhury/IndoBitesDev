# Generated by Django 5.0.2 on 2024-08-12 11:34

import datetime
import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongapp', '0062_alter_booking_day_alter_chatgroup_groupname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime(2024, 8, 12, 17, 4, 38, 677265)),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='groupname',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hall',
            name='ammenity',
            field=models.CharField(choices=[('Buffet', 'Buffet'), ('Cafeteria-Style', 'Cafeteria-Style:'), ('Pre-Set Service', 'Pre-Set Service'), ('Cocktail-Style', 'Cocktail-Style'), ('Cabaret', 'Cabaret'), ('Banquet-Style', 'Banquet-Style'), ('Dinner-Dance', 'Dinner-Dance'), ('Exhibition', 'Exhibition'), ('Plated', 'Plated'), ('Meeting-Style', 'Meeting-Style')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hallbookings',
            name='booking_id',
            field=models.CharField(blank=True, default=shortuuid.main.ShortUUID.uuid, max_length=100, unique=True),
        ),
    ]
