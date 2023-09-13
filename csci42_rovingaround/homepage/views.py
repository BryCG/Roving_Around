from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views import View
from .forms import BookingForm
from login.models import Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# from django.db import models
import sys
sys.path.insert(0, 'csci42_rovingaround/login/')
from login import models
from login.models import Booking

# Create your views here.
# https://learndjango.com/tutorials/django-search-tutorial
class UserListView(ListView):
	def get(self, request):
		current_user = request.user
		all_profile = models.Profile.objects.exclude(status="Dog Owner")
		recommended_profiles = models.Profile.objects.filter(
			Q(city__icontains=current_user.profile.city) | Q(province__icontains=current_user.profile.province)).exclude(status="Dog Owner")
		query = request.GET.get("q")
		search_profiles = None
		if (query != None):
			search_profiles = models.Profile.objects.filter(
				Q(city__icontains=query) | Q(province__icontains=query)).exclude(status="Dog Owner")
		context = {
			"recommended_profiles": recommended_profiles,
			"search_profiles": search_profiles,
			"all_profile": all_profile
		}
		return render(request, 'homepage/home.html', context)

def displayprofile(request, id):#though the name is displayprofile i realized its easier to use user
	user_profile = User.objects.get(pk=id)
	#description = models.Description.objects.get(user=user_profile)
	context = {
		"user" : user_profile,
		#"description" : description
	}
	return render(request, "homepage/profile-display.html", context)

def booking(request, id):
	if request.method == 'POST':
		booking = BookingForm(request.POST)
		# booking.dogsitter = User.objects.get(pk=id)
		# booking.dogowner = User.objects.get(pk=id)
		if booking.is_valid():
			new_booking = booking.save()
			return redirect('/')	
	booking = BookingForm()
	return render(request, 'homepage/booking.html', {'booking': booking})

@login_required
def homepage(request):
	# if request.user.is_authenticated:
	# 	return render(request=request, template_name='homepage/home.html')
	# else:
		return render(request=request, template_name='homepage/home.html')

def accept_bookings(request):

	bookings = Booking.objects.filter(accepted = False)
	context = {
		'bookings' : bookings
	}

	if request.method == 'POST':
		booking_id = request.POST.get('booking_id')
		action = request.POST.get('action')

		if booking_id and action:
			booking = Booking.objects.get(pk=booking_id)

			if action ==  'accept':
				booking.accepted = True
			elif action == 'decline':
				booking.accepted = False
			
			booking.save()
	
	return render(request, 'homepage/accepting.html', context)
#https://stackoverflow.com/questions/70943013/how-can-i-display-all-the-users-on-my-html-page
#https://stackoverflow.com/questions/23139657/django-get-all-users