# Generated by Django 4.1 on 2022-09-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_rename_notification_created_time_notification_notif_created_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notifi_status',
            new_name='notif_status',
        ),
    ]
