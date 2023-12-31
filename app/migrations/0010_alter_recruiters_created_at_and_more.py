# Generated by Django 4.1.6 on 2023-05-05 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_recruiters_primary_colour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiters',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 11, 11, 5, 168833)),
        ),
        migrations.AlterField(
            model_name='recruiters',
            name='primary_colour',
            field=models.CharField(blank=True, default='#008D96', max_length=250),
        ),
        migrations.AlterField(
            model_name='recruiters',
            name='secondary_colour',
            field=models.CharField(blank=True, default='#c8dddf', max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_colour',
            field=models.CharField(blank=True, default='#008D96', max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_colour',
            field=models.CharField(blank=True, default='#c8dddf', max_length=250),
        ),
    ]
