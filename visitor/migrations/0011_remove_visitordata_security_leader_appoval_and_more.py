# Generated by Django 4.2 on 2023-10-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0010_auto_20230929_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitordata',
            name='security_leader_appoval',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='security_leader_appoval_reason',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='security_leader_appoval_time',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='security_manager_approval',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='security_manager_approval_reason',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='security_manager_approval_time',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='team_leader_approval',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='team_leader_approval_reason',
        ),
        migrations.RemoveField(
            model_name='visitordata',
            name='team_leader_approval_time',
        ),
    ]
