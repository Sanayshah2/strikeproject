# Generated by Django 3.1.3 on 2021-03-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='count_table',
            name='time_stamp',
            field=models.DateTimeField(default=None),
        ),
    ]
