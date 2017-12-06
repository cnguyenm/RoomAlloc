from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Location, Room, Reservation, Profile, Feedback

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'year', 'remain']
    ordering = ['user', 'major', 'year']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'location', 'capacity', 'is_reservable']
    search_fields = ['name', 'tech', 'capacity']
    
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'time_start', 'time_end']
    

admin.site.register(Feedback)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Location)

admin.site.register(Reservation, ReservationAdmin)