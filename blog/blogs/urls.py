"""Defines URL patterns for blogs"""

from django.urls import re_path

from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.home, name='home'),

    # Page for adding blog posts
    re_path(r'^add_post/$', views.add_post, name='add_post'),

    # Page for editing a post
    re_path(r'^edit_post/(?P<post_id>\d+)$', views.edit_post, name='edit_post'),
]