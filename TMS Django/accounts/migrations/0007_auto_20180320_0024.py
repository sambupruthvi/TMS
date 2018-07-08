# Generated by Django 2.0.3 on 2018-03-20 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='sup_name',
            field=models.CharField(default='sup_name', max_length=200),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
    ]