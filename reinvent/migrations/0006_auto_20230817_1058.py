# Generated by Django 3.2.12 on 2023-08-17 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reinvent', '0005_rename_requestday_reinventdata_appliedday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reinventdata',
            old_name='appliedday',
            new_name='applied_day',
        ),
        migrations.RenameField(
            model_name='reinventdata',
            old_name='lateday',
            new_name='late_day',
        ),
    ]
