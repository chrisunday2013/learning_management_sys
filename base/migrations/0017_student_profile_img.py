# Generated by Django 4.1 on 2022-09-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_studentassignment_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='student_profile_imgs/'),
        ),
    ]