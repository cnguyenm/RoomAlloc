"""
Forms for reservation: 
* Creation
* Update
* Delete
"""

from django import forms

from roomalloc.models import Profile, Reservation
from roomalloc.util import validation


time_help_text = "\
    <ul> \
    <li> Minute should be 30 or 0 </li>\
    <li> Second should be 0 </li>\
    <li> Date should be in future </li>\
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
    time_start = forms.DateTimeField(
        help_text = time_help_text,
        validators=[validation.validate_time_round_up],
        widget = forms.DateTimeInput(
            attrs = {'class' : 'form-control datetime-input'}
        ),
    )
    
    time_end = forms.DateTimeField(
        help_text = time_help_text,
        validators=[validation.validate_time_round_up],
        widget = forms.DateTimeInput(
            attrs = {'class' : 'form-control datetime-input'}
        ),
    )
    
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
        Makesure time_end > time_start
        """
        time_start  = self.cleaned_data.get("time_start")
        time_end    = self.cleaned_data.get("time_end")
        
        
        print(type(time_start))
        return time_start