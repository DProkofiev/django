# Generated by Django 3.0.3 on 2020-02-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstsiteapp', '0003_auto_20200221_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='name',
            field=models.CharField(default=1, max_length=4, unique=True),
            preserve_default=False,
        ),
    ]