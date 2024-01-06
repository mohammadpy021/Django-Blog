from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Member
from accounts.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q
'''
Custom mixins
'''
class FieldMixin(object):

    def dispatch(self, request, *args, **kwargs):

        self.fields= ["title",
                "description",
                "slug",
                "category",
                "is_special",
                "photo",
                "status",#it has to be here 
                ]
        if  request.user.is_superuser:
            self.fields += ["author"]
        elif not request.user.is_author:
            return redirect("accounts:home")   
        return super().dispatch(request, *args, **kwargs)
    
class FormValidMixin(object):
    ''' save current user as author if he is not superuser'''
    def form_valid(self, form):
        if not self.request.user.is_superuser:
            form.instance.author = self.request.user
      
            if  form.instance.status != "I":
                form.instance.status = "D"
        
        return super().form_valid(form)
        


class AccessMixin(object):
    def dispatch(self, request,pk, *args, **kwargs):
        articles = get_object_or_404(Member, pk=pk)
        if  request.user.is_superuser  or (articles.status in ["D", "B"] and articles.author == request.user) :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("صفحه مورد نظر پیدا نشد")


class AuthorsAccess(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else :
            return redirect("accounts:profile")
class DeleteMixin(object):
    def dispatch(self, request,pk, *args, **kwargs):
        articles = get_object_or_404(Member, pk=pk)
        if  request.user.is_superuser or (articles.status in ["D", "B"] and articles.author == request.user) :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما دسترسی به این صفحه را ندارید")
        
    
class RedirectUserLoggedInMixin(object):
    redirect_authenticated_user = False
    def dispatch(self, request , *args, **kwargs) :
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            return redirect(redirect_to)
            
        return super().dispatch(request, *args, **kwargs)

