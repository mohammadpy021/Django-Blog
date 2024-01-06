# Generated by Django 4.2.2 on 2023-12-25 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('slug', models.SlugField(default='', help_text='آدرس slug', max_length=255, unique=True, verbose_name='نامک')),
                ('position', models.IntegerField(default=1, verbose_name='پوزیشن')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش داده شود')),
                ('parent', models.ForeignKey(blank=True, help_text='subcategory', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category', verbose_name=' زیردسته')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان سایت در قسمت navbar', max_length=255, verbose_name='عنوان سایت ')),
            ],
            options={
                'verbose_name': 'عنوان سایت',
                'verbose_name_plural': 'عنوان سایت',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('slug', models.SlugField(default='', help_text='آدرس slug', max_length=255, unique=True, verbose_name='نامک')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('P', 'انتشار'), ('D', 'پیش نویس'), ('I', 'درحال بررسی'), ('B', 'برگشت داده\u200cشده')], max_length=1, verbose_name='وضعیت')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='تصاویر')),
                ('is_special', models.BooleanField(default=False, verbose_name='مقاله ویژه')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها ',
            },
        ),
    ]
