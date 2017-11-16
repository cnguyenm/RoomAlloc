from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
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

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    
    # create new profile
    if created:
        Profile.objects.create(user=instance)
    
    # save    
    instance.profile.save()
    
    
    
    
    