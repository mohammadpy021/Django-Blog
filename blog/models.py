from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from extensions.utils import jalali_convertor
# from django.contrib.auth.models import User
from accounts.models import User
from django.urls import reverse 


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='P')
    def active(self):
        return self.filter(status=True)
    
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True, verbose_name=_(" زیردسته"), help_text="subcategory")
    title= models.CharField(max_length=255, verbose_name=_("عنوان"))
    slug = models.SlugField(max_length=255, unique=True, default='', help_text=("آدرس slug"),verbose_name=_("نامک")) 
    position = models.IntegerField(verbose_name=_("پوزیشن"), default=1) 
    status = models.BooleanField(default=True, verbose_name=_("نمایش داده شود"))
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["parent__id", "position"]
    def __str__(self):
        return self.title
    objects = ArticleManager()
    
class Member(models.Model):# Articles
    STATUS = [
        ("P", "انتشار"),         # publish
        ("D", "پیش نویس"),       # draft
        ("I", "درحال بررسی"),    # investigate
        ("B", "برگشت داده‌شده"),  # back
    ]
    title= models.CharField(max_length=255, verbose_name=_("عنوان"))
    description = models.TextField(blank=True, null=True, verbose_name=_("توضیحات"))
    slug = models.SlugField(max_length=255, unique=True, default='', help_text=("آدرس slug"),verbose_name=_("نامک")) 
    category = models.ManyToManyField(Category, verbose_name=_("دسته بندی ها"), related_name='articles', blank=True)
    author = models.ForeignKey(User,verbose_name=_("نویسنده"),on_delete=models.CASCADE,null=True,related_name='articles',)
    
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ انتشار"))
    # updated_at = models.DateTimeField(auto_now=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_("تاریخ انتشار"))#False: showing the calender
    updated_at = jmodels.jDateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=_("وضعیت"))
    photo = models.ImageField(upload_to="photo/", verbose_name=_("تصاویر"), blank=True, null=True)
    is_special = models.BooleanField(default=False, verbose_name= _("مقاله ویژه") )
    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقاله ها ")
    def __str__(self):
        return self.title
    def get_categories(self):
        return  ",".join([i.title for i in self.category.filter(status=True)])

    get_categories.short_description = _("دسته بندی ها")
    objects = ArticleManager()
    def get_absolute_url(self): # new
        return reverse('accounts:home')

class Settings(models.Model):
    title= models.CharField(max_length=255, verbose_name=_("عنوان سایت "), help_text="عنوان سایت در قسمت navbar")
    class Meta:
        verbose_name = _("عنوان سایت")
        verbose_name_plural = _("عنوان سایت")
    def __str__(self):
        return self.title








