# Generated by Django 2.1.3 on 2019-06-06 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190606_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bought_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Buyer', to_field='buyername', verbose_name='購入者'),
        ),
    ]
