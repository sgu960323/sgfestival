# Generated by Django 2.2.5 on 2019-09-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190921_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='fri',
            field=models.IntegerField(default=0),
        ),
    ]