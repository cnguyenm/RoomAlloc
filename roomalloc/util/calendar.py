"""
Some helper class, functions to deal with 
 * data structure
 * render calendar template

"""

from django.utils import timezone

class CalendarEvent():
    
    """
    Helper class when rendering html
    
    """
    event_id= 0     # int
    title   = None  # str
    start   = None  # str
    end     = None  # str
    url     = None  # str
    
def get_room_events(room):
    """
    get events to render to webpage
    @param room: <model> room model
    @return events: list<CalendarEvent>
    """
    
    # get room schedule
    reservations = room.reservation_set.all()
    
    # convert reservations into calendar_events
    # ex: '2017-11-09T16:00:00'
    events = []
    event  = None
    for r in reservations:
        
        # get localtime
        start = timezone.localtime(r.time_start)
        end   = timezone.localtime(r.time_end)
        
        event = CalendarEvent()
        event.event_id = r.id
        event.title = "Booked"
        event.start = start.strftime("%Y-%m-%dT%H:%M:%S")
        event.end   = end.strftime("%Y-%m-%dT%H:%M:%S")
        events.append(event)
        
    return events
    
    
    