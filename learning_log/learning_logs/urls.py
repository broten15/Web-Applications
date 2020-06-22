"""Defines URL patterns for learning_logs"""

from django.urls import re_path 

from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),

    # Show all topics
    re_path(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]