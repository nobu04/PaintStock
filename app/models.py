from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings




class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        elif not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True, null=True,)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Buyer(models.Model):

    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )


    buyername = models.CharField(
        name='buyername',
        max_length=200,
        unique=True,
        verbose_name='氏名',
    )

    gender = models.IntegerField(
        verbose_name='性別',
        choices=GENDER_CHOICES,
        default=1
    )

    age = models.IntegerField(
        verbose_name='年齢'
    )

    related_user = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        blank=False
    )


    def __str__(self):
        return self.buyername
        
    class Meta:
        verbose_name = 'バイヤー'
        verbose_name_plural = 'バイヤー'

class Item(models.Model):

    CATEGORY_CHOICES = (
        (1, '作品'),
        (2, '額縁'),
    )

    STATUS_CHOICES = (
        (1, '所持'),
        (2, '売却'),
        (3, '廃棄'),
    )
    
    name = models.CharField(
        verbose_name='タイトル',
        max_length=200,
    )

    bought_by = models.CharField(
        verbose_name='購入者名',
        max_length=20,
    )


    image = models.ImageField(
        verbose_name='画像',
        upload_to='pictures/',
        blank=True,
        null=True,
        )


    status = models.IntegerField(
        verbose_name='ステータス',
        choices=STATUS_CHOICES,
        default=1,
    )    

    size = models.CharField(
        verbose_name='サイズ',
        max_length=200,
        default='20角'
    )

    category = models.IntegerField(
        verbose_name='カテゴリー',
        choices=CATEGORY_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True,
    )

    created_by = models.ForeignKey(User, 
        on_delete=models.CASCADE)

    bought_by = models.ForeignKey(Buyer, 
        verbose_name='購入者',
        to_field='buyername', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True)

