# Generated by Django 4.2.6 on 2023-10-12 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stomatolog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 10, 34, 40, 723622, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='appointment_time',
            field=models.TimeField(),
        ),
    ]