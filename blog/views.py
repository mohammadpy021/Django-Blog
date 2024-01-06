from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Category, User
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from accounts.mixins import AccessMixin
from django.db.models import  Q
from datetime import datetime , timedelta
from django.utils.translation import activate
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class ArticleListView(ListView):
    queryset = Member.objects.published()
    paginate_by = 3 


class ArticleDeatil(DetailView):
    # template_name = "blog/post.html"
    # context_object_name = "object_list"
    def get_object(self):
        self.slug = self.kwargs["slug"]
        article = get_object_or_404(Member, slug=self.slug, status="P")
        return article

class ArticlePreview(AccessMixin, DetailView):
    def get_object(self):
        self.pk = self.kwargs["pk"]
        return Member.objects.get(pk= self.pk)


class CategoryView(ListView):
    paginate_by = 1
    template_name = "blog/category.html"
    def get_queryset(self):
        self.slug = self.kwargs["slug"]
        category = get_object_or_404(Category, status=True, slug = self.slug)#Category.objects.all() won't work we need only one object
        return category.articles.published()

class AuthorView(ListView):
    paginate_by = 3 
    template_name = "blog/author_list.html"
    def get_queryset(self):
        global author
        userename = self.kwargs["author"]
        author = get_object_or_404(User,  username = userename)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] =  author
        return context

class SearchView(ListView):
    paginate_by = 1
    template_name = "blog/search_list.html"
    def get_queryset(self):
        global search
        search = self.request.GET.get('q', "")  #q is specified in the <input name='q'... and url: http://.../search/?q=< words > 
        return Member.objects.published().filter(Q(description__icontains=search) | Q(title__icontains=search))
    def get_context_data(self, **kwargs): #sending extra context
        context = super().get_context_data(**kwargs)
        context["search_title"] =  search
        return context
    
    
    