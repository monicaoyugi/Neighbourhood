from django.db import models
import datetime as DateTimeField
from django.contrib.auth.models import User
# Create your models here.
class Neighbourhood(models.Model):
    '''
    neighbourhood class and its methods
    ''' 
    neighbourhood_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    number_of_estates = models.CharField(max_length=50)

    def __str__(self):
      return self.neighbourhood_name

class Business(models.Model):
    '''
    business class and its model
    '''
    business_name = models.CharField(max_length=50)
    business_email = models.EmailField(null=True)
    business_id = models.ForeignKey(Neighbourhood, blank = True, on_delete=models.CASCADE )

class Business(models.Model):
    '''
    Business class and its model
    '''
    # cover_image = models.ImageField((upload_to = 'business/', null=True, blank=True)
    name = models.CharField(max_length=50)
    business_email = models.EmailField(null=True)
    business_id = models.ForeignKey(Neighbourhood, blank = True, on_delete=models.CASCADE )
    estate = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    '''
    normal user profile model and its methods
    '''
    profile_picture = models.ImageField(blank=True)
    name_user = models.TextField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)

class Posts(models.Model):
    '''
    model for alerts/meetings & posts
    '''
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=80)
    message = models.TextField(max_length=200, null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

