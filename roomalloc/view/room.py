"""
room.py:

Deal with view for room
* Detail
* Reserve
* Schedule ??

"""
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from roomalloc.const import Template as T
from roomalloc.models import Room, Location, Reservation
from roomalloc.util import calendar
from roomalloc.form.reservation import ReserveCreationForm

# convert to local timezone


@login_required
def explore(request):
    """
    Display list of rooms
    """
    
     # get query string
    search = request.GET.get('search','')
    
    # get query_set
    rooms = Room.objects.filter( Q( name__icontains=search) | Q(location__name__icontains=search) | Q(tech__icontains=search) )
    
    context = {
        "nbar" : "room_explore",
        "rooms": rooms
    }
    
    # render
    return render(request, T.ROOM_EXPLORE, context)
    
    
@login_required
def detail(request, room_id):
    """
    Detail of room:
    * spec
    * schedule
    """
    
    # get room
    room = get_object_or_404(Room, pk=room_id)
    
    # get room schedule
    events = calendar.get_room_events(room)
    
    # get datetime today
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    
    # context
    context = {
        "nbar"   : "room_explore",
        "room"   : room,
        "today"  : today,
        "events" : events,
    }
    
    return render(request, T.ROOM_DETAIL, context)
    
@login_required
def reserve(request, room_id):
    """
    Reserve room for user
    Display a form
    """
    # var
    form = None
    room = get_object_or_404(Room, pk=room_id)
    error_msg = None
    
    # calendar context
    events = calendar.get_room_events(room)
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    
    # handle post
    if request.method == "POST":
        form = ReserveCreationForm(request.POST, room=room, user=request.user)
        if form.is_valid():
            
            # save reservation
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.room = room
            reservation.save()
            
            return redirect( 
                reverse("roomalloc:room_confirm", 
                kwargs={'res_id' : reservation.id}
            ) )
    else:
        form = ReserveCreationForm(room=room, user=request.user)
    
    # context
    context = {
        "nbar"   : "room_explore",
        "events" : events,
        "today"  : today,
        "room"   : room,
        "form"   : form
    }
    
    return render(request, T.ROOM_RESERVE, context)
    
@login_required
def confirm(request, res_id):
    
    res = get_object_or_404(Reservation, pk=res_id)
    
    
    return render(request, T.ROOM_CONFIRM, {"res":res})