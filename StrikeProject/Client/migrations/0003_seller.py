# Generated by Django 3.0.7 on 2021-03-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_count_table_time_stamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='Your Name')),
                ('product', models.CharField(default='', max_length=40, verbose_name='Product Name')),
            ],
        ),
    ]