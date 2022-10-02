from django.contrib import admin
from .models import Profile, LoggedInUsers, UserLocationsModel

# Register your models here.
admin.site.register(Profile)
admin.site.register(LoggedInUsers)
admin.site.register(UserLocationsModel)