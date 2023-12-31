# Generated by Django 4.1.6 on 2023-05-05 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_recruiters_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiters',
            name='master_primary_colour',
            field=models.CharField(blank=True, default='#008D96', max_length=250),
        ),
        migrations.AddField(
            model_name='recruiters',
            name='master_secondary_colour',
            field=models.CharField(blank=True, default='#c8dddf', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='master_primary_colour',
            field=models.CharField(blank=True, default='#008D96', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='master_secondary_colour',
            field=models.CharField(blank=True, default='#c8dddf', max_length=250),
        ),
        migrations.AlterField(
            model_name='recruiters',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 12, 38, 17, 300967)),
        ),
    ]
