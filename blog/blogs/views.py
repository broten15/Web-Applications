from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogForm

# Create your views here.

def home(request):
    """The home page that contains all my blog posts"""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/home.html', context)

def add_post(request):
    """A page for adding new blog posts"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlogForm
    else:
        # POST data submitted; process data
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:home'))
    
    context = {'form':form}
    return render(request, 'blogs/add_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post"""
    blog_post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Initial request; prefill form with existing post
        form = BlogForm(instance=blog_post)
    else:
        # POST data submitted; process data
        form = BlogForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:home'))
    
    context = {'form':form, 'blog_post':blog_post}
    return render(request, 'blogs/edit_post.html', context)


