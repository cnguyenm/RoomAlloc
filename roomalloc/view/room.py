"""
room.py:

Deal with view for room
* Detail
* Reserve
* Schedule ??

"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from roomalloc.const import Template as T
from roomalloc.models import Room, Location


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
    context = {
        "nbar" : "room_explore",
        "room" : room
    }
    
    return render(request, T.ROOM_DETAIL, context)