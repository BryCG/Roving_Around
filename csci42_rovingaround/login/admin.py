from django.contrib import admin
from .models import Profile, Dog, Booking, Rating, Description

admin.site.register(Profile)
admin.site.register(Dog)
admin.site.register(Rating)
admin.site.register(Description)
admin.site.register(Booking)

