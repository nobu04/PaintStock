# Generated by Django 2.1.3 on 2019-06-06 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_buyer_registered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='registered_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
