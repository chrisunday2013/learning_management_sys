# Generated by Django 4.1 on 2022-10-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
