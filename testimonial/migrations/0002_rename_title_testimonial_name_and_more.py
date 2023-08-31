# Generated by Django 4.1.5 on 2023-08-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='designation',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='images',
            field=models.FileField(null=True, upload_to='testimonial'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='top_property',
            field=models.BooleanField(default=0),
        ),
    ]
