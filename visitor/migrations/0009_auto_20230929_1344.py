# Generated by Django 3.2.12 on 2023-09-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0008_auto_20230929_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitordata',
            name='security_leader_appoval_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='visitordata',
            name='security_manager_approval_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='visitordata',
            name='team_leader_approval_time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
