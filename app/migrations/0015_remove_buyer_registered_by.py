# Generated by Django 2.1.3 on 2019-06-06 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190606_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='registered_by',
        ),
    ]