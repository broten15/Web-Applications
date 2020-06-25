"""Defines URL patterns for pizzeria"""

from django.urls import re_path

from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),

    # Show all pizzas
    re_path(r'^pizzas/$', views.pizzas, name='pizzas'),
    
    # Detail page for a single pizza
    re_path(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza')
]