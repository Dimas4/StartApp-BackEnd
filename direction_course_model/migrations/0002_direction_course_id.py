# Generated by Django 2.1.1 on 2018-09-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction_course_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='course_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]