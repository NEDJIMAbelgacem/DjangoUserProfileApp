# Generated by Django 4.1.1 on 2022-10-02 15:45

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_portfolio', '0005_userlocationsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocationsmodel',
            name='user_locations',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point, srid=4326),
        ),
    ]
