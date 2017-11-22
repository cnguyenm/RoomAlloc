
"""
Contains form validators
"""

import datetime
from django.core.exceptions import ValidationError


def validate_time_round_up(user, room):
    """
    reservation validators
    * min: 0, 30; 
    * second: 0
    * cannot in the past
    * cannot reserve 2times a day
    * not interfere with other events
    @param time: <datetime.datetime> 
    @param user: <model>
    @param room: <model>
    """
    def inner_function(time):
        # get datetime today
        now = datetime.datetime.now()
        today = now.strftime("%Y/%m/%d")
        
        # get 
        
        # get datetime submit
        minute = time.minute
        second = time.second
        submit_day = time.strftime("%Y/%m/%d")
        
        errors  = []
        
        # check error
        if (minute != 30 and minute != 0):
            errors.append(
                ValidationError('Minute should be 30, or 0', code='error1')
            )
        
        if (second != 0):
            errors.append(
                ValidationError('Second should be 0', code='error2')
            )
        
        if (submit_day <= today):
            errors.append(
                ValidationError('Date should be future', code='error3')
            )
        
        if (len(errors) > 0):
            raise ValidationError(errors)
            
    return inner_function
    
    
def validate_purdue_email(value):
    """
    validators: Check if purdue email
    @param value: <string>
    """
    
    if "@purdue.edu" not in value:
        raise ValidationError(
            'Not Purdue email', code='invalid'
        )
    

def validate_room_amount(room):
    """
    validators: Check estimated_amount of room is valid 
    * amount > room.capacity * 25%
    * amount < room.capacity * 125%
    @param room: <model> 
    @param amount: <int>
    """
    def inner_function(amount):
        
        # check param
        if room is None:
            print("Room: None")
            return
        
        capacity = room.capacity
        if (amount < capacity * 0.25):
            raise ValidationError("Amount too small", code="error_too_small")
    
        if (amount > capacity * 1.25):
            raise ValidationError("Amount too big", code="error_too_big")
            
    return inner_function