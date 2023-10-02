# Generated by Django 3.2.12 on 2023-09-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0004_alter_visitordata_pic_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitordata',
            old_name='approval_status',
            new_name='security_admin_approval',
        ),
        migrations.AddField(
            model_name='visitordata',
            name='security_team_leader_appoval',
            field=models.CharField(default='Requested', max_length=20),
        ),
        migrations.AddField(
            model_name='visitordata',
            name='your_team_manager_approval',
            field=models.CharField(default='Requested', max_length=20),
        ),
    ]
