"""
user.py:

Deal with view for normal user

"""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from roomalloc.const import Template as T
from roomalloc.models import Room, Location

@login_required
def home(request):
    return render(request, T.USER_HOME, {})

# list of reservation
@login_required
def reserve(request):
    return HttpResponse("list of reservations")



    

    