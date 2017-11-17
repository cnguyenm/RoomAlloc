
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from roomalloc.models import Profile

class SignUpForm(UserCreationForm):
    
    # models.User already has field email
    # doing this will put email into model directly
    email = forms.EmailField(max_length=254, help_text="Purdue email")
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
        

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    
    #email = forms.EmailField(help_text='Purdue email')
    grad_date = forms.DateField(help_text='Format: YYYY-MM-DD')
    
    class Meta:
        model = Profile
        fields = ('grad_date', 'year', 'major')