# Generated by Django 4.1.5 on 2023-08-18 12:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0003_rename_top_property_testimonial_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
