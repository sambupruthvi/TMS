# Generated by Django 2.0.3 on 2018-03-23 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180323_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='emp_name',
        ),
    ]
