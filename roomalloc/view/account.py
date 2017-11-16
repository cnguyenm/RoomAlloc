
"""
account.py:

Deal with operation with account

"""
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse

from roomalloc.const import Template
from roomalloc.const import TplConst as T
# Create your views here.

def signup(request):
    
    #if request.method == 'POST':
    return render(request, Template.ACC_SIGNUP, {T.NBAR:"signup"})
    
    
def log_in(request):
    return render(request, Template.ACC_LOGIN, {T.NBAR:"login"})
    
def log_out(request):
    return HttpResponse("Log out");