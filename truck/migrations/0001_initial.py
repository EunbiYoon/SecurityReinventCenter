# Generated by Django 3.2.12 on 2023-09-19 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=255, null=True)),
                ('license_plate', models.CharField(max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('truck_number', models.CharField(max_length=255, null=True)),
                ('direct_cntr', models.CharField(max_length=255, null=True)),
                ('in_trailer', models.CharField(max_length=255, null=True)),
                ('seal_number', models.CharField(max_length=255, null=True)),
                ('checkin_at', models.DateTimeField(null=True)),
                ('checkout_at', models.DateTimeField(blank=True, null=True)),
                ('out_trailer', models.CharField(max_length=255, null=True)),
                ('load_status', models.CharField(max_length=255, null=True)),
                ('checkin_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkin_pic', to=settings.AUTH_USER_MODEL)),
                ('checkout_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_pic', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Truck Tracking Data',
            },
        ),
    ]
