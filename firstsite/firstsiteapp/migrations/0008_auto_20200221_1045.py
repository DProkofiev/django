# Generated by Django 3.0.3 on 2020-02-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstsiteapp', '0007_auto_20200221_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='description',
        ),
        migrations.RemoveField(
            model_name='year',
            name='year',
        ),
    ]