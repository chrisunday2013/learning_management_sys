# Generated by Django 4.1 on 2022-09-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_teacher_profile_img_alter_courserating_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]