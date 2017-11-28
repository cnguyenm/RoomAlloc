
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

from roomalloc.form.account import (
    UserForm, ProfileForm, SignUpForm, SignInForm
)

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
            
            # add to group
            normal_group, create = Group.objects.get_or_create(name='normal')
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
    

def update_profile(request):
    
    # user form
    form1 = None
    user_model = None
    
    # profile form
    form2 = None
    profile_model = None
    
    msg = None
    
    if (request.method == "POST"):
        form1 = UserForm(request.POST, instance=request.user)
        form2 = ProfileForm(request.POST, instance=request.user.profile)
        
        if form1.is_valid() and form2.is_valid():
            
            # get model
            user_model = form1.save()
            user_model.refresh_from_db() # load the profile
            
            profile_model = form2.save(commit=False)
            profile_model.user = user_model
            
            # save model
            profile_model.save()
            
            msg = "Updated successfully"
            
            
    else:
        form1 = UserForm(instance=request.user)
        form2 = ProfileForm(instance=request.user.profile)
    
    context = {
        "nbar"  : "update_profile",
        "msg"   : msg,
        "form1" : form1,
        "form2" : form2
    }
    
    return render(request, Template.ACC_PROFILE, context)

def log_out(request):
    logout(request)
    return redirect(reverse("roomalloc:index"))
    

def is_user_normal(user):
    return user.groups.filter(name=GroupName.NORMAL).exists()
    
    
    