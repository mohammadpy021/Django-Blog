from django import template
from ..models import Category, Settings, Category, Member
from django.db.models import Count, Q
from datetime import datetime , timedelta
from django.contrib.contenttypes.models import ContentType
from urllib.parse import urlencode
register = template.Library()



@register.simple_tag()
def title():
    name =  Settings.objects.all().first() if Settings.objects.all() else "سایت جنگو"
    return name


@register.inclusion_tag("blog/partial/navbar.html")
def navbar():#use {%navbar%} in templates
    return {
        "categories": Category.objects.filter(status= True)
    }
@register.inclusion_tag("blog/partial/sidebar.html")
def popular_articles():#use {%popular_articles%} in templates
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Member.objects.published()\
        .annotate(count=Count('hits',filter=Q(articlehit__created__gt = last_month))).order_by('-count')[:5],
        "title" : "مقاله های پربازدید ماه "
    }
@register.inclusion_tag("blog/partial/sidebar.html")
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Member.objects.published()\
        .annotate(count=Count('comments',filter=Q(comments__posted__gt = last_month) and Q(comments__content_type_id = ContentType.objects.get(app_label="blog", model="member").id))).order_by('-count')[:5],
        "title" : "داغ ترین مطالب"
    }
@register.inclusion_tag("blog/partial/sidebar.html")
def stars_articles():# I couldn't set the query based on highest star ratings in last *30 days*(this month)
    last_month = datetime.today() - timedelta(days=30)
    return {
        "articles": Member.objects.published().order_by('-ratings__average','-ratings__published')[:5],
        # .annotate(count=Count('ratings', filter=Q(ratings__average__gt = 0) and Q(ratings__published__gt = last_month) )).order_by('-count')[:5], # this doenst work and i dont know why!
        "title" : "پرستاره ترین مقاله ها"
    }
@register.inclusion_tag("registration/partial/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link" : f"accounts:{link_name}",
        "content": content,
        "classes" : classes
    }


#pagination tags
@register.simple_tag
def url_replace (request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
