from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:home'))

def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else: 
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # Log the user in and direct them to the home page
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:home'))

    context = {'form':form}
    return render(request, 'users/register.html', context)


    

