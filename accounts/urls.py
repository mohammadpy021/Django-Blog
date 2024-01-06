from django.contrib.auth import views
from .views import (HomeList,
                    ArticleCreate,
                    ArticleUpdate,
                    ArticleDelete,
                    Profile,
                    Login,
                    # activate,
                    Register,
                    SearchList
 )
from django.urls import path
from django.urls import reverse_lazy


app_name = "accounts"
# urlpatterns = [
    # path("login/", Login.as_view(redirect_authenticated_user=True), name="login"),
#     path("logout/", views.LogoutView.as_view(), name="logout"),
#     path(
#         "password_change/", PasswordChange.as_view(), name="password_change"
#     ),
#     path(
#         "password_change/done/",
#         views.PasswordChangeDoneView.as_view(),
#         name="password_change_done",
#     ),
#     # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
#     # path(
#     #     "password_reset/done/",
#     #     views.PasswordResetDoneView.as_view(),
#     #     name="password_reset_done",
#     # ),
#     # path(
#     #     "reset/<uidb64>/<token>/",
#     #     views.PasswordResetConfirmView.as_view(),
#     #     name="password_reset_confirm",
#     # ),
#     # path(
#     #     "reset/done/",
#     #     views.PasswordResetCompleteView.as_view(),
#     #     name="password_reset_complete",
#     # ),
# ]

urlpatterns = [

    path("", HomeList.as_view(), name="home"),
    path("search/", SearchList.as_view(), name="search"),
    path("create/", ArticleCreate.as_view(), name="article-create"),
    path("update/<int:pk>", ArticleUpdate.as_view(), name="article-update"),
    path("delete/<int:pk>", ArticleDelete.as_view(), name="article-delete"),
    path("profile/", Profile.as_view(), name="profile"),

]