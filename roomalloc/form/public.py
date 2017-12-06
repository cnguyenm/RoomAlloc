

from django import forms


from roomalloc.models import  Feedback


class FeedbackForm(forms.ModelForm):
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs = {'placeholder':'Subject', 'class':'form-control'}
        )
    )
    
    comments = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs = {'placeholder':'Comments, everything is confidential', 'class':'form-control'}
        )
    )
    
    class Meta:
        model = Feedback
        fields = ('subject', 'comments')