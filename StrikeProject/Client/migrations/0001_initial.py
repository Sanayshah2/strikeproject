# Generated by Django 3.1.3 on 2021-03-16 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=40, verbose_name='Product Name')),
                ('company', models.CharField(default='', max_length=40, verbose_name='Company Name')),
                ('capacity', models.IntegerField(default=0, verbose_name="Inventory's Capacity (Number of Units)")),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Count_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('accuracy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(default='', max_length=40, verbose_name="Seller's name")),
                ('message', models.TextField(blank='true', null='True', verbose_name='Message to the seller (optional)')),
                ('quantity', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Client.client')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
