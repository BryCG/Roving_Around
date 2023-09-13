from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import sys
sys.path.insert(0, 'csci42_rovingaround/login/')
from login.models import Profile, Description, Rating, Dog, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['dogsitter', 'dogowner', 'date_start', 'date_end', 'payment']