"""
public.py:
Render the public page
"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from roomalloc.const import Template
from roomalloc.const import TplConst as T

def index(request):
    return render(request, Template.PUBLIC_INDEX, {T.NBAR:"index"})
    
def about(request):
    return render(request, Template.PUBLIC_ABOUT, {T.NBAR :"about"})
    
def contact(request):
    return render(request, Template.PUBLIC_CONTACT, {T.NBAR:"contact"})
    
def feedback(request):
    return HttpResponse("Submit feedback")
    
