from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json 
from django.utils.translation import gettext_lazy as _


from .models import *


def index(request):
    all_posts= Post.objects.all().order_by("id").reverse()

     # Display 10 posts per page
    paginator = Paginator(all_posts,10) 
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    
    # retrieves the IDs of all posts that the user has liked and stores these 
    # IDs in the liked_posts list, depending on that value of Like/Unlike button changes 
    if request.user.is_authenticated:
        for post in page_posts:
            post.is_liked_by_user = post.likes.filter(user=request.user).exists()
    else:
        for post in page_posts:
            post.is_liked_by_user = False

    return render(request, "network/index.html", {
        "page_posts": page_posts,
        "post_count": all_posts.count(),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
# creating new post and saving it in the database
@login_required
def newpost(request):
    if request.method=="POST":
        content=request.POST['content']
        user= User.objects.get(pk=request.user.id)
        post=Post(content=content, user=user)
        post.save()
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request, "network/newpost.html")

# @login_required  
def profile_page(request, user_id):
    profile = User.objects.get(pk=user_id)
    all_posts = Post.objects.filter(user=profile).order_by("-id")
    post_count = all_posts.count()

    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    profile_post = paginator.get_page(page_number)

    # Safely set is_liked_by_user for each post
    for post in profile_post:
        if request.user.is_authenticated:
            post.is_liked_by_user = post.likes.filter(user=request.user).exists()
        else:
            post.is_liked_by_user = False

    # Only allow follow/unfollow if logged in and not viewing own profile
    is_following = False
    if request.user.is_authenticated and profile != request.user:
        is_following = request.user.follows.filter(pk=profile.pk).exists()

    if request.method == "POST" and request.user.is_authenticated and profile != request.user:
        current_user_profile = request.user
        if current_user_profile.follows.filter(pk=profile.pk).exists():
            current_user_profile.follows.remove(profile)
            is_following = False
        else:
            current_user_profile.follows.add(profile)
            is_following = True
        current_user_profile.save()
        # (re-render as below)

    return render(request, "network/profile_page.html", {
        "profile": profile,
        "post_count": post_count,
        "profile_post": profile_post,
        "is_following": is_following,
    })

#displaying following page contains posts posted by whom user follows
# @login_required
def home_page(request):
    # Get posts from users the current user follows
    if request.user.is_authenticated:
        all_posts = Post.objects.filter(user__in=request.user.follows.all()).order_by("-id")
    else:
        all_posts = Post.objects.none()  # or show all posts, or an empty list
    
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    # Set is_liked_by_user for each post
    for post in page_posts:
        if request.user.is_authenticated:
            post.is_liked_by_user = post.likes.filter(user=request.user).exists()
        else:
            post.is_liked_by_user = False

    return render(request, "network/home.html", {
        "page_posts": page_posts,
        "post_count": all_posts.count(),
    })

# Editing post function and updating database with Json
@login_required
def edit_post(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(pk=post_id)
        edit_post.content = data["content"]
        edit_post.save()
        return JsonResponse({"message": "Change successfull", "data": data["content"]})

# Like/Unlike post and updating database with Json
# @login_required
def toggle_like(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse({'redirect': '/login'}, status=401)
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, post=post)
    
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    like_count = post.likes.count()

    return JsonResponse({"liked": liked, "post_id": post_id, "like_count": like_count})

# @login_required
def following_page(request):
    followed_users = request.user.follows.all()

    return render(request, "network/following.html", { 
        "followed_users": followed_users,  # Pass this to the template
    })