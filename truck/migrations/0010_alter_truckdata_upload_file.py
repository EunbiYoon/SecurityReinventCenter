# Generated by Django 4.2 on 2023-09-26 02:02

from django.db import migrations, models
import truck.models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0009_truckdata_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckdata',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to=truck.models.upload_location),
        ),
    ]
