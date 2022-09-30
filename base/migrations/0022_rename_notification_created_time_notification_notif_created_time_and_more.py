# Generated by Django 4.1 on 2022-09-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_notification_notification_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notification_created_time',
            new_name='notif_created_time',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='notification_for',
            new_name='notif_for',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='notification_subject',
            new_name='notif_subject',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_status',
        ),
        migrations.AddField(
            model_name='notification',
            name='notifi_status',
            field=models.BooleanField(default=False, verbose_name='Notification Status'),
        ),
    ]