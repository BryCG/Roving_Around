from django.urls import path
from . import views
from .views import HomePageView
from .views import profile
#import sys
#sys.path.append('/csci42_rovingaround/homepage/')
#from homepage import views
#from homepage.views import UserListView

urlpatterns = [
    #path("homepage", UserListView.as_view(), name="homepage"),
    path("register/", views.login_request, name="registration"),
    path("logout", views.logout_request, name= "logout"),
    path("", views.logger_request, name="login"),
    #path('profile/<int:pk>', profile, name='users-profile'),
    path('profile', profile, name="users-profile")
    
    
]

app_name = "login" 