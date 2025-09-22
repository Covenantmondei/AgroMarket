from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('FARMER', 'Farmer'),
    ('BUYER', 'Buyer'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='BUYER')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class Farmer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    farm_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.farm_name} - {self.profile.user.username}"