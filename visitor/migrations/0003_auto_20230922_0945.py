# Generated by Django 3.2.12 on 2023-09-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_alter_visitordata_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitordata',
            name='status',
        ),
        migrations.AddField(
            model_name='visitordata',
            name='approval_status',
            field=models.CharField(default='Requested', max_length=20),
        ),
        migrations.AddField(
            model_name='visitordata',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
