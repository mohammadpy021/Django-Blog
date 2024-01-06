from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from blog.models import Member
from .models import User
from .mixins import FormValidMixin, FieldMixin, AccessMixin, DeleteMixin, AuthorsAccess, RedirectUserLoggedInMixin
from .forms import ProfileForm, SignupForm, ArticleForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
#mail confirm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.db.models import  Q

class HomeList(LoginRequiredMixin,AuthorsAccess, ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Member.objects.all()
        else:
            queryset = Member.objects.filter(author= self.request.user)
        return queryset 

class SearchList(HomeList):
    template_name =   "registration/search_list.html"
    def get_queryset(self) :
        global query_arg 
        query_arg = self.request.GET.get('s', "")     #s is specified in the <input name='s'... and url: http://.../?s=< words > 
        if self.request.user.is_superuser:
            queryset = Member.objects.filter(Q(description__icontains=query_arg) | Q(title__icontains=query_arg))
        else :
            queryset = Member.objects.filter(author= self.request.user).filter(Q(description__icontains=query_arg) | Q(title__icontains=query_arg))
        return queryset
    def get_context_data(self, **kwargs): #sending extra context
        context = super().get_context_data(**kwargs)
        context["search_title"] = query_arg
        return context

class ArticleCreate(LoginRequiredMixin,FieldMixin, FormValidMixin, CreateView):#FieldMixin
    template_name = "registration/article-create-update.html"
    model = Member
    # form_class = ArticleForm
    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        if self.request.user.is_superuser:
            # form.fields['author'].queryset = User.objects.filter(Q(is_author = True)| Q(is_superuser= True))                   #way 1
            form.fields['author'].queryset  = form.fields['author'].queryset.filter(Q(is_author = True)| Q(is_superuser= True))  #way 2
        return form

class ArticleUpdate(LoginRequiredMixin,SuccessMessageMixin, AccessMixin,FieldMixin, FormValidMixin, UpdateView):#FieldMixin
    template_name = "registration/article-create-update.html"
    model = Member
    success_message = "محتوا با موفقیت آپدیت شد."
    # form_class = ArticleForm
    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        if self.request.user.is_superuser:
            # form.fields['author'].queryset = User.objects.filter(Q(is_author = True)| Q(is_superuser= True))                   #way 1
            form.fields['author'].queryset  = form.fields['author'].queryset.filter(Q(is_author = True)| Q(is_superuser= True))  #way 2
        return form

class ArticleDelete(DeleteMixin, DeleteView):
    model = Member
    success_url = reverse_lazy("accounts:home")
    template_name = "registration/article-delete.html"

#User
class Profile(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("accounts:home")
    def get_form_kwargs(self): #sending kwargs to the forms.py:61
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs.update({'user': self.request.user})
        return kwargs
    def get_object(self):#in this case we dont need to write the pk in the urls
        return User.objects.get(pk=self.request.user.pk)



class Login(LoginView):
    def get_success_url(self):
        if not self.request.user.is_author:
            return reverse("accounts:profile")
        else:
            return reverse("accounts:home")



class Register(RedirectUserLoggedInMixin,CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm
    def get_success_url(self) -> str:
        return reverse("accounts:profile")

    

    
