# Generated by Django 4.1.5 on 2023-07-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_alter_properties_content_alter_properties_highlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertiesimage',
            name='feature_image',
            field=models.BooleanField(default=0),
        ),
    ]