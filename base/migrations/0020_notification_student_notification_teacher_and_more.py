# Generated by Django 4.1 on 2022-09-29 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.student'),
        ),
        migrations.AddField(
            model_name='notification',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.teacher'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_for',
            field=models.CharField(max_length=250, verbose_name='Notification For'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_status',
            field=models.BooleanField(default=False, verbose_name='Notification For'),
        ),
    ]
