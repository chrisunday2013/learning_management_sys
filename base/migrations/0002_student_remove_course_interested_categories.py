# Generated by Django 4.1 on 2022-09-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=18)),
                ('address', models.TextField()),
                ('interested_categories', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='interested_categories',
        ),
    ]
