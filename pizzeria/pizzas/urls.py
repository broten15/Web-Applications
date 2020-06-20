"""Defines URL patterns for pizzeria"""

from django.urls import re_path

from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index')
]