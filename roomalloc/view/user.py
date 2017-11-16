"""
public.py:
Render the public page
"""

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'roomalloc/user/user_home.html', {})