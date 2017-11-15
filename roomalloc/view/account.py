
"""
account.py:

Deal with operation with account

"""
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from roomalloc.const import Template
from roomalloc.const import TplConst as T


def signup(request):
    return render(request, Template.ACC_SIGNUP, {T.NBAR:"signup"})
    
    
def login(request):
    return render(request, Template.ACC_LOGIN, {T.NBAR:"login"})
    
def logout(request):
    return HttpResponse("Log out");