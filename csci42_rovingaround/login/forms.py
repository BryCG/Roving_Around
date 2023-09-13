from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Description, Rating, Dog, Booking


DEMO_CHOICES =(
    ("Dog Owner", "Dog Owner"),
    ("Dog Sitter", "Dog Sitter"),
    ("Dog Walker" , "Dog Walker")
)

# Create your forms here.

class NewLoginForm(UserCreationForm):
	status = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices = DEMO_CHOICES,)
	province = forms.CharField(required=True, max_length=50)
	city = forms.CharField(required=True, max_length=50)
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name" ,"email", "password1", "password2", "province", "city", "status")
