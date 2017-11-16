
"""
account.py:

Deal with operation with account

"""
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from roomalloc.forms import UserForm, ProfileForm, SignUpForm

from roomalloc.const import Template
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
            user.save()
            
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_passwd)
            login(request, user)
            
            return redirect('/user/')
        
    else:
            form = SignUpForm()
        
    return render(request, Template.ACC_SIGNUP, {T.NBAR:"signup", 'form':form})
    
    
def log_in(request):
    return render(request, Template.ACC_LOGIN, {T.NBAR:"login"})
    
def log_out(request):
    return HttpResponse("Log out");