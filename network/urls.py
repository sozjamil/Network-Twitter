
from django.urls import path

from . import views

urlpatterns = [
    # path("follow_unfollow/", views.follow_unfollow, name="follow_unfollow"),
    path("profile_page/<int:user_id>", views.profile_page, name="profile_page"),
    path("newpost", views.newpost, name="newpost"),

    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
