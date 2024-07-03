from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse


from .models import *


def index(request):
    all_posts= Post.objects.all().order_by("id").reverse()
    paginator = Paginator(all_posts,10)  # Display 10 posts per page

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "all_posts":all_posts,
        "page_posts": page_posts
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

def newpost(request):
    if request.method=="post":
        content=request.POST['content']
        user= User.objects.get(pk=request.user.id)
        post=Post(content=content, user=user)
        post.save()
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request, "network/newpost.html")

def profile_page(request, user_id):
    user=User.objects.get(pk=user_id)
    all_posts= Post.objects.filter(user=user).order_by("id").reverse()
    
    #follower and following
    following=Follow.objects.filter(user=user).count()
    followers=Follow.objects.filter(user_follower=user).count()
    
    try:
        checkFollow= followers.filter(user=User.objects.get(pk=request.user.id))
        if len(checkFollow) != 0:
            isFollowing =  True
        else:
            isFollowing = False
    except:
        isFollowing=False


    # pagination: Display 10 posts per page
    paginator = Paginator(all_posts,10)  
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, "network/profile_page.html", {
        "page_posts": page_posts,
        "username":user.username,
        "following": following,
        "followers":followers,
        "isFollowing": isFollowing,
        "user_profile":user
    })