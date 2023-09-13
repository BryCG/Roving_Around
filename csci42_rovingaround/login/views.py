from django.shortcuts import  render, redirect
from .forms import NewLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, User, Booking
from .forms import NewLoginForm

class HomePageView(View):
    def homepage(request):
        return render(request=request, template_name='login/home.html')


def login_request(request):
	if request.method == "POST":
		form = NewLoginForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			status = form.cleaned_data.get('status')
			province = form.cleaned_data.get('province')
			city = form.cleaned_data.get('city')
			user = User.objects.get(username=username)
			user_data = Profile.objects.create(user=user, status=status, province=province, city=city)
			user_data.save()
			messages.success(request, "Registration successful." )
			return redirect("login:login")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewLoginForm()
	return render (request, "login/registration.html", {'registration_form': form})



def logger_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/logger.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login:login")


@login_required
def profile(request):
	current_user = request.user
	if (current_user.profile.status == "Dog Owner"):
		bookings = Booking.objects.filter(dogowner=current_user)
	else:
		bookings = Booking.objects.filter(dogsitter=current_user)
	context = {
		"user" : current_user,
		"all_bookings": bookings
	}
	return render(request, 'login/profile.html', context)