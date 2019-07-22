from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Item

admin.site.register(User, UserAdmin)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'
