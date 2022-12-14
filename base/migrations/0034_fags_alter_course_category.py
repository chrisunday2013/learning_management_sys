# Generated by Django 4.1 on 2022-10-12 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_course_course_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=700)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': '16. FAQs',
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_courses', to='base.coursecategory'),
        ),
    ]
