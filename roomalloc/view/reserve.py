"""
reserve.py:

Deal with list of reserve for user

"""
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from roomalloc.const import Template as T
from roomalloc.models import Reservation
from roomalloc.util import calendar

@login_required
def display(request):
    """
    Display calendar of user's reservations
    todo: 
    css for class'fc-time-grid-event fc-v-event fc-event fc-start fc-end'
    """
    
    # get list of events
    events = calendar.get_event_list(request.user)
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    
    context = {
        "nbar" : "res_display",
        "events" : events,
        "today"  : today,
    }
    return render(request, T.RES_LIST, context)

@login_required
def detail(request, res_id):
    """
    Display reservation detail, user can delete
    """
    
    has_delete = None
    res = get_object_or_404(Reservation, pk=res_id)
    
    if request.method == "POST":
        
        # delete, after delete, res object still there
        # only record in db is lost
        res.delete() 
        has_delete = True
        
    context = {
        "nbar"       : "res_display",
        "has_delete" : has_delete,
        "res"        : res
    }
    
    return render(request, T.RES_DETAIL, context)