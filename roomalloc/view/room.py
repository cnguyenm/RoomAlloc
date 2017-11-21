"""
room.py:

Deal with view for room
* Detail
* Reserve
* Schedule ??

"""
import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from roomalloc.const import Template as T
from roomalloc.models import Room, Location
from roomalloc.helper import CalendarEvent

@login_required
def explore(request):
    """
    Display list of rooms
    """
    # get query_set
    rooms = Room.objects.all()
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
    reservations = room.reservation_set.all()
    
    # convert reservations into calendar_events
    # ex: '2017-11-09T16:00:00'
    events = []
    event  = None
    for r in reservations:
        event = CalendarEvent()
        event.event_id = r.id
        event.title = "Booked"
        event.start = r.time_start.strftime("%Y-%m-%dT%H:%M:%S")
        event.end   = r.time_end.strftime("%Y-%m-%dT%H:%M:%S")
        events.append(event)
    
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
    
    """
    
    return HttpResponse("hello")