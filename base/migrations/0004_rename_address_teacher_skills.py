# Generated by Django 4.1 on 2022-09-08 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='address',
            new_name='skills',
        ),
    ]