# Generated by Django 2.2.5 on 2019-09-19 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0006_auto_20190919_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodtruck',
            old_name='ftRating',
            new_name='generalRating',
        ),
        migrations.AlterField(
            model_name='foodtruckcomment',
            name='ftCommentTimeStamp',
            field=models.DateField(default=datetime.datetime(2019, 9, 19, 17, 57, 5, 331317, tzinfo=utc)),
        ),
    ]