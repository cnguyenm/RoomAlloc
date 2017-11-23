"""
Forms for reservation: 
* Creation
* Update
* Delete
"""

import datetime

from django import forms

from roomalloc.models import Profile, Reservation
from roomalloc.util import validation


time_start_help_text = "\
    <ul> \
    <li> Minute should be 30 or 0 </li>\
    <li> Second should be 0 </li>\
    <li> Date should be in future </li>\
    </ul>"
    
time_end_help_text = "\
    <ul> \
    <li> Minute should be 30 or 0 </li>\
    <li> Second should be 0 </li>\
    <li> Date should be in future </li>\
    <li> Occur after time_start </li>\
    <li> In 1 day with time_start </li>\
    </ul>"


amount_help_text = "\
    <ul> \
    <li> Estimated amount of people </li>\
    <li> Greater than 0 </li>\
    <li> Fit within room max-capacity </li>\
    </ul>"

class ReserveCreationForm(forms.ModelForm):
    """
    Reserve Creation Form 
    
    """
    # instance variable: Room model
    room = None
    user = None
    
    def __init__(self, *args, **kwargs):
        # get key
        if 'room' in kwargs:
            self.room = kwargs.pop('room')
        
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
            
        # run super.init
        super(ReserveCreationForm, self).__init__(*args, **kwargs)
        self.fields['amount'].validators = \
            [validation.validate_room_amount(self.room),]
            
        self.fields['time_start'].validators = \
            [validation.validate_time_round_up(self.user, self.room),]
        
        self.fields['time_end'].validators = \
            [validation.validate_time_round_up(self.user, self.room),]
            
    # time_start
    time_start = forms.DateTimeField(
        help_text = time_start_help_text,
        widget = forms.DateTimeInput(
            attrs = {'class' : 'form-control datetime-input'}
        ),
    )
    
    # time_end
    time_end = forms.DateTimeField(
        help_text = time_end_help_text,
        widget = forms.DateTimeInput(
            attrs = {'class' : 'form-control datetime-input'}
        ),
    )
    
    # amount
    amount = forms.IntegerField(
        help_text = amount_help_text,
        widget = forms.NumberInput(
            attrs = {'class' : 'form-control'}
        )
    )
    
    
    
    class Meta:
        model = Reservation
        fields = ('time_start', 'time_end', 'amount')
        
    def clean_time_end(self):
        """
        Auto-run 
        check: time_end > time_start
        check: time_end, time_start in 1 day
        """
        
        # get time submit
        time_start  = self.cleaned_data.get("time_start")
        time_end    = self.cleaned_data.get("time_end")
    
        # error_lit
        errors = []
        
        # check time_end > time_start
        if (time_start > time_end):
            errors.append(forms.ValidationError(
                "time_start greater than time_end",
                code="error_time_start_greater"
            ))
        
        # check time_start, time_end on same day
        if (time_start.date() != time_end.date()):
            errors.append(forms.ValidationError(
                "time_start, time_end on different day",
                code="error_diff_day"
            ))
        
        # check time_end <= time_start + 3h
        if (time_end > time_start + datetime.timedelta(hours=3)):
            errors.append(forms.ValidationError(
                "Event should less than 3 hours",
                code="error_too_long"
            ))
        
        if (len(errors) > 0):
            raise forms.ValidationError(errors)
        
        return time_end