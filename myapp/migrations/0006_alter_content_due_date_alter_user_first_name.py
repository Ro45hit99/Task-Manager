# Generated by Django 4.0.4 on 2022-06-02 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201022_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 0, 33, 58, 552252)),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
