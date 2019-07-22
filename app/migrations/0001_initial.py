# Generated by Django 2.1.3 on 2019-06-03 09:40

import app.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', app.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyername', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, verbose_name='メールアドレス')),
                ('gender', models.IntegerField(choices=[(1, '男性'), (2, '女性')], default=1, verbose_name='性別')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('adress', models.CharField(max_length=200, verbose_name='住所')),
            ],
            options={
                'verbose_name': 'バイヤー',
                'verbose_name_plural': 'バイヤー',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures/', verbose_name='画像')),
                ('status', models.IntegerField(choices=[(1, '所持'), (2, '売却'), (3, '廃棄')], default=1, verbose_name='ステータス')),
                ('size', models.CharField(default='20角', max_length=200, verbose_name='サイズ')),
                ('category', models.IntegerField(choices=[(1, '作品'), (2, '額縁')], default=1, verbose_name='カテゴリー')),
                ('memo', models.TextField(blank=True, max_length=300, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL, verbose_name='作家')),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='app.Item', verbose_name='作品'),
        ),
    ]
