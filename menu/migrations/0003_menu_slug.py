# Generated by Django 4.1.5 on 2023-08-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_location_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
