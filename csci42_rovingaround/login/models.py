from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg
from datetime import datetime

# Create your models here.

DEMO_CHOICES =(
    ("Dog Owner", "Dog Owner"),
    ("Dog Sitter", "Dog Sitter"),
    ("Dog Walker" , "Dog Walker")
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices = DEMO_CHOICES, default="Dog Owner")
    province = models.CharField(max_length = 50, default="Metro Manila")
    city = models.CharField(max_length = 50, default="Quezon City")

    def __str__(self):
        return self.user.username


#Dog Owner
class Dog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, default='')
    color = models.CharField(max_length=100)
    weight = models.IntegerField()
    behavior = models.TextField()
    dietary_restrictions = models.TextField()
    comments = models.TextField()
    
    def __str__(self):
        return f"{self.name}"


#Dog sitter/walker
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.profile} : {self.rating} by {self.user}"


class Description(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(default='')
    description = models.TextField(default='')
    rates = models.TextField(default='')
    
    def average_rating(self) -> float: #avg ratings
        return Rating.objects.filter(description=self).aggregate(Avg("rating"))["rating__avg"] or 0
    
    def __str__(self):
        return f"{self.user} description"


#bookings
class Booking(models.Model):
    cash = 'Cash'
    card = 'Card'
    OL = 'Online Payment'
    
    dogsitter = models.ForeignKey(User, related_name='sitter', on_delete=models.CASCADE)
    dogowner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    date_start = models.DateTimeField(default=datetime.now, blank=True)
    date_end = models.DateTimeField(default=datetime.now, blank=True)
    # dropoff_time = models.TimeField(default='10:00')
    # pickup_time = models.TimeField(default='10:00')
    
    payment_choices = [
        (cash, 'Cash'),
        (card, 'Card'),
        (OL, 'Online Payment')
    ]

    payment = models.CharField(
        max_length=20,
        choices=payment_choices,
        default=cash)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.pk}"
    

#https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c