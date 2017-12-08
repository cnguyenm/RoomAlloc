from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Feedback(models.Model):
    subject = models.CharField(max_length=200)
    comments = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.subject

class Visitor(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
        
class Profile(models.Model):
    
    # information
    UNDERGRAD   = 'UNDER'
    GRAD        = 'GRAD'
    PROF        = 'PROF'
    YEAR_CHOICE = (
        (UNDERGRAD, 'UNDERGRAD'),
        (GRAD, 'GRADUATE'),
        (PROF, 'PROFESSOR')
    )
    
    # 1-1 key with user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # other information
    major = models.CharField(max_length = 200)
    grad_date = models.DateField(null=True, blank=True)
    
    year  = models.CharField(
        max_length = 10,
        choices = YEAR_CHOICE,
        default = UNDERGRAD
    )
    
    # penalty count
    remain = models.IntegerField(default=3, help_text="Chances for penalty") # penalty remains
    
    def __str__(self):
        return str(self.user.username) + "-profile"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    
    # create new profile
    if created:
        Profile.objects.create(user=instance)
    
    # save    
    instance.profile.save()
    
    
    
    
class Location(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    
    # foreign key
    location        = models.ForeignKey('Location', on_delete=models.CASCADE)
    
    # fields
    name            = models.CharField(max_length=200, default="", unique=True)
    capacity        = models.IntegerField(
        help_text="Max capacity of room",
        validators  = [MinValueValidator(1)]
    )
    tech            = models.TextField(help_text="Technology is room")
    is_reservable   = models.BooleanField()
    
    def __str__(self):
        return str(self.location) + "/" + str(self.name)
        
        
    
class Reservation(models.Model):
    
    # key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    
    # fields
    time_start  = models.DateTimeField()
    time_end    = models.DateTimeField()
    amount      = models.IntegerField(help_text="Estimated Amount of people") #estimated amount
    reason      = models.CharField(max_length=200, help_text="Reason summarized", default="Study")
    
    
    # real time
    real_amount = models.IntegerField(help_text="Real amout of people at room", default=0)
    
    def __str__(self):
        return str(self.user.username) + "-" + str(self.room)
        
    