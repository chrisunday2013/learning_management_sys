# Generated by Django 4.1 on 2022-09-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_courserating_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='student_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
