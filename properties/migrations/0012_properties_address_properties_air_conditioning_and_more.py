# Generated by Django 4.1.5 on 2023-07-14 07:52

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_remove_properties_lat_remove_properties_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='air_conditioning',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='balcony',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='basement',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='bathroom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='bedroom',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='cooling',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='properties',
            name='dining_room',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='diswasher',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='featured',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='fireplace',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='garage',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='lawn',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='microwave',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='parking',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='property_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='property_size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='refrigerator',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='short_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='properties',
            name='start_form',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='top_property',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='tv_cable',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='type',
            field=models.CharField(choices=[('FOR RENT', 'For Rent'), ('FOR SALE', 'For Sale')], default='for_sale', max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='wifi',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='properties',
            name='year_of_bulit',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
