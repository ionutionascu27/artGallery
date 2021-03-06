from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddressMixin(models.Model):

    class Meta:
        abstract = True
    
    address_line1 = models.CharField(max_length=128, blank=True, default='')
    address_line2 = models.CharField(max_length=128, blank=True, default='')
    city = models.CharField(max_length=64, blank=True, default='')
    county = models.CharField(max_length=64, blank=True, default='')
    country = models.CharField(max_length=64, blank=True, default='')
    zip_code = models.CharField(max_length=8, blank=True, default='')

class Profile(AddressMixin, models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images', default='/default/default_avatar.png')
    PROFILE_CHOICES = (('ARTIST', 'Artist'), ('CUSTOMER', 'Customer'))
    profile_type = models.CharField(max_length=24, choices=PROFILE_CHOICES, blank=True, default='')
    phone = models.CharField(max_length=24, null=False, blank=True, default='')
    stripe_id = models.CharField(max_length=256, blank=True)
    subscr_id = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.user.username

   