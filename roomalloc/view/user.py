"""
user.py:

Deal with view for normal user

"""

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'roomalloc/user/user_home.html', {})

# list of reservation    
def reserve(request):
    return HttpResponse("list of reservations")
    
def explore(request):
    return HttpResponse("Explore study room")
    
    