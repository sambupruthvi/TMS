# Generated by Django 2.0.2 on 2018-03-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_timesheet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='project',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='project',
            field=models.CharField(default='No Project', max_length=100),
        ),
    ]
