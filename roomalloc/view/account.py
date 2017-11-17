
"""
account.py:

Deal with operation with account

"""
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import Group

from roomalloc.forms import UserForm, ProfileForm, SignUpForm, SignInForm

from roomalloc.const import Template, GroupName
from roomalloc.const import TplConst as T
# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            
            # save to db
            user = form.save()
            user.refresh_from_db() # load the profile
            user.profile.email = form.cleaned_data.get('email')
            
            # add to group
            normal_group = Group.objects.get(name='normal')
            user.groups.add(normal_group)
            
            # save
            user.save()
            
            # log user in
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_passwd)
            login(request, user)
            
            return redirect( reverse('roomalloc:user_home') )
        
    else:
            form = SignUpForm()
        
    return render(request, Template.ACC_SIGNUP, {T.NBAR:"signup", 'form':form})
    
    
def log_in(request):
    
    # default form
    form = SignInForm(request.POST)
    error_msg = None
    
    # if post
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                return redirect( reverse('roomalloc:user_home') )
            
            else:
                error_msg = "Wrong username, or password"
    
    else:
        form = SignInForm()
    
    return render(request, Template.ACC_LOGIN, 
        {T.NBAR:"login", 'form':form, 'error_msg':error_msg}
    )
    
    
def log_out(request):
    logout(request)
    return redirect(reverse("roomalloc:index"))
    

def is_user_normal(user):
    return user.groups.filter(name=GroupName.NORMAL).exists()
    
    
    