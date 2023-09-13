from django.urls import path
from . import views
from .views import UserListView, displayprofile, booking, accept_bookings

import sys
sys.path.append('/csci42_rovingaround/login/')
from login import views
from login.views import logout_request

app_name = "homepage"   


urlpatterns = [
    path('', UserListView.as_view(), name="homepage"),
    path('profile-display/<int:id>', displayprofile, name='displayprofile'),
    path('booking/<int:id>', booking, name='booking'),
    path("logout", views.logout_request, name= "logout"),
    path('accepting/', accept_bookings, name="accepting"),
] 