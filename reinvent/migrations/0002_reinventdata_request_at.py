# Generated by Django 3.2.12 on 2023-08-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reinvent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reinventdata',
            name='request_at',
            field=models.DateField(auto_now=True),
        ),
    ]
