# Generated by Django 4.2.6 on 2023-10-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stomatolog', '0003_remove_application_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='application',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]