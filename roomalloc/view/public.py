"""
public.py:
Render the public page
"""

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

from roomalloc.const import Template
from roomalloc.const import TplConst as T
from roomalloc.models import Feedback
from roomalloc.form.public import FeedbackForm


def index(request):
    return render(request, Template.PUBLIC_INDEX, {T.NBAR:"index"})
    
def about(request):
    return render(request, Template.PUBLIC_ABOUT, {T.NBAR :"about"})
    
def contact(request):
    return render(request, Template.PUBLIC_CONTACT, {T.NBAR:"contact"})
    
def fd_conf(request):
    return render(request, Template.PUBLIC_FD_CONF, {})

def feedback(request):
    
    if request.method == "POST":
        
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            
            # save feedback
            feedback = form.save()
            return redirect( reverse('roomalloc:fd_conf') )
            
    
    return HttpResponse("Submit feedback")
    
    
