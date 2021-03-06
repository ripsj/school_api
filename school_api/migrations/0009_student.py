# Generated by Django 2.2.6 on 2019-11-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0008_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('courses', models.ManyToManyField(blank=True, to='school_api.Course')),
            ],
        ),
    ]
