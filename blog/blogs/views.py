from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm

# Create your views here.

def home(request):
    """The home page that contains all my blog posts"""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/home.html', context)

@login_required
def add_post(request):
    """A page for adding new blog posts"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlogForm
    else:
        # POST data submitted; process data
        form = BlogForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:home'))
    
    context = {'form':form}
    return render(request, 'blogs/add_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post"""
    blog_post = get_object_or_404(BlogPost, id=post_id)
    check_post_owner(request, blog_post)

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

def check_post_owner(request, blog_post):
    """Check to see of post owner matches the current user"""
    if blog_post.owner != request.user:
        raise Http404


