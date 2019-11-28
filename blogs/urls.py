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

# class based urls below
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

# function based views use this statement
from . import views

urlpatterns = [
    # routes for function based views
    # path('', views.home, name='blogs-home'),
    # path('index/', views.home, name='blogs-home'),
    # path('about/', views.about, name='blogs-about'),
    #  end routes for function based views


# create, read, update, delete
# class based urls below
#     uses template home.html and this has to be converted using .as_view() function invoked
    path('', PostListView.as_view(), name='blogs-home'),

    # uses post_detail.html template
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Expects post_form.html template. it does not expect post_create like you might think django uses post_form instead
    path('post/new/', PostCreateView.as_view(), name='post-create'),

   # also uses post_form.html template and shares it with the above post/new
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blogs-about'),

]

