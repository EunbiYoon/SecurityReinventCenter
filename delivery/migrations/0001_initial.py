# Generated by Django 3.2.12 on 2023-08-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCodeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_data', models.CharField(max_length=255)),
                ('arriving_at', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.CharField(max_length=255)),
                ('receiver_check', models.BooleanField(default=False)),
                ('admin_check', models.BooleanField(default=False)),
                ('receiver_at', models.DateTimeField(blank=True, null=True)),
                ('admin_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'QR Scanning Data',
            },
        ),
    ]
