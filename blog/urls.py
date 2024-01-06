from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
   
    
    path("", views.ArticleListView.as_view(), name="members"),
    path("members/<slug:slug>/", views.ArticleDeatil.as_view(), name="detail"),
    path("preview/<int:pk>/", views.ArticlePreview.as_view(), name="preview"),
    path("category/<slug:slug>/", views.CategoryView.as_view(), name="category"),
    path("author/<slug:author>/", views.AuthorView.as_view(), name="author"),#url gets author name
    path("search/", views.SearchView.as_view(), name="search"),#url gets author name
    # path("category/<slug:slug>/page/<int:page>/", views.category, name="category"),
    
    
] 

