# Generated by Django 4.0.4 on 2022-06-14 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_content_due_date_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 20, 42, 12, 86494)),
        ),
    ]
