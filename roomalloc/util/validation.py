
"""
Contains form validators
"""

import datetime
from django.core.exceptions import ValidationError

# reservation validators
# * min: 0, 30; 
# * second: 0
# * cannot in the past
# time_end - time_start > 30 min


def validate_time_round_up(time):
    """
    Check min: 0, 30 
    sec: 0
    date: in future
    @param time: <datetime.datetime> 
    
    """
    # get datetime today
    now = datetime.datetime.now()
    today = now.strftime("%Y/%m/%d")
    
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
        
    
    
def validate_purdue_email(value):
    """
    Check if purdue email
    @param value: <string>
    """
    
    if "@purdue.edu" not in value:
        raise ValidationError(
            'Not Purdue email', code='invalid'
        )
    
