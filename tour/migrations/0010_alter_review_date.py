# Generated by Django 4.1.1 on 2022-11-11 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 18, 1, 0, 436730), null=True),
        ),
    ]
