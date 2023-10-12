# Generated by Django 4.1.6 on 2023-05-03 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_assessment_name_alter_recruiters_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='url',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='recruiters',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 11, 17, 39, 477609)),
        ),
    ]