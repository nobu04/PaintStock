# Generated by Django 2.1.3 on 2019-06-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190603_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, '男性'), (2, '女性')], verbose_name='性別'),
        ),
    ]