# Generated by Django 2.1.3 on 2019-06-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190606_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='buyername',
            field=models.CharField(max_length=200, unique=True, verbose_name='氏名'),
        ),
    ]