# Generated by Django 2.0.2 on 2018-03-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0013_auto_20180313_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='numero',
            field=models.IntegerField(auto_created=True),
        ),
    ]
