# Generated by Django 2.2.6 on 2019-11-02 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0004_auto_20191102_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='lastCourse',
            new_name='previousCourse',
        ),
    ]
