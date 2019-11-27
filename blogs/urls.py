"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blogs/', include('blogs.urls'))
"""
from django.contrib import admin
# from django.urls import path,include
# from . import views
#
#
# #function view import statement
#
#
# urlpatterns = [
#     path('', views.index, name='blogs-home'),
#     path('index/', views.index, name='blogs-home'),
#     path('about/', views.about, name='blogs-about'),
#
# ]


from django.contrib import admin
from django.urls import path, include
from . import views

# function view import statement

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from . import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('index/', views.home, name='blogs-home'),
    path('about/', views.about, name='blogs-about'),

    # create, read, update, delete

    path('', PostListView.as_view(), name='blogs-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blogs-about'),

]


