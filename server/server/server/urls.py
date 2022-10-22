"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_json),
    path('user_tweets/', views.user_tweets),
    path('login/', views.login),
    path('oauth/', views.oauth),
    path('retweet/', views.retweet),
    path('unretweet/', views.unretweet),
    path('like/', views.like),
    path('unlike/', views.unlike),
    path('create_tweet/', views.create_tweet),
    path('reply/', views.reply),
    path('delete_tweet/', views.delete_tweet),
    path('follow/', views.follow),
    path('unfollow/', views.unfollow),
    path('get_followers/', views.get_followers),
    path('get_following/', views.get_following),
    path('unfollow/', views.unfollow),
    path('search_tweets/', views.search_tweet),
    path('get_profile/', views.get_profile),
    #path('search_users/', views.search_user),
]
