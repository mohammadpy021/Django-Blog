from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False, verbose_name="وضعیت‌‌نویسندگی")
    special_user = jmodels.jDateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
    def is_special_user(self):
        if self.special_user > timezone.datetime.now():#timezone.now() will count base on day rather than minute
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description ="وضعیت‌کاربر ویژه"
    # def get_absolute_url(self):
    #     return reverse("accounts:home")
    
