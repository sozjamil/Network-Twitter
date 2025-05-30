
from django.urls import path

from . import views

urlpatterns = [
    path('toggle_like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("following_page/", views.following_page, name="following_page"),
    path("profile_page/<int:user_id>", views.profile_page, name="profile_page"),
    path("newpost", views.newpost, name="newpost"),
    path("home/", views.home_page, name="home_page"),


    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
