# Generated by Django 2.1.1 on 2018-09-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='direction',
            field=models.ManyToManyField(blank=True, to='direction_course_model.Direction'),
        ),
        migrations.AlterField(
            model_name='course',
            name='home_work',
            field=models.ManyToManyField(blank=True, to='homework_model.HomeWork'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lesson',
            field=models.ManyToManyField(blank=True, to='test_student_model.Lesson'),
        ),
        migrations.AlterField(
            model_name='course',
            name='likes',
            field=models.ManyToManyField(blank=True, to='like_model.Like'),
        ),
        migrations.AlterField(
            model_name='course',
            name='student_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='upcoming_webinar',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='work',
            field=models.ManyToManyField(blank=True, to='test_student_model.Work'),
        ),
    ]