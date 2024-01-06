from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


# UserAdmin.fieldsets +=  (('Extra Fields', {'fields': ('is_author', )}),)

_list = list(UserAdmin.fieldsets[2][1]['fields'])
_list[3:3] = ["is_author", "special_user"]
UserAdmin.fieldsets[2][1]['fields'] = tuple(_list)

UserAdmin.list_display += ("is_author", "is_special_user")

admin.site.register(User, UserAdmin)




