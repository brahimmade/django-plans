# Generated by Django 3.2.11 on 2022-01-13 19:17

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0009_auto_20210303_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_city',
            field=models.CharField(blank=True, max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer_country',
            field=django_countries.fields.CountryField(blank=True, default='PL', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer_street',
            field=models.CharField(blank=True, max_length=200, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer_zipcode',
            field=models.CharField(blank=True, max_length=200, verbose_name='Zip code'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_country',
            field=django_countries.fields.CountryField(blank=True, default='PL', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_street',
            field=models.CharField(blank=True, max_length=200, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='shipping_zipcode',
            field=models.CharField(blank=True, max_length=200, verbose_name='Zip code'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='default',
            field=models.BooleanField(db_index=True, default=None, help_text='Both "Unknown" and "No" means that the plan is not default', null=True, unique=True),
        ),
    ]
