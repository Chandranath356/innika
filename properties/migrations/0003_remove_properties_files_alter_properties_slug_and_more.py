# Generated by Django 4.1.5 on 2023-05-03 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_remove_properties_picture_properties_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='files',
        ),
        migrations.AlterField(
            model_name='properties',
            name='slug',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='properties',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='PropertiesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(null=True, upload_to='')),
                ('properties', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
        ),
    ]
