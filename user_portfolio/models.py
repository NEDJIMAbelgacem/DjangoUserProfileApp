from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos.point import Point
from django.contrib.gis.geos.collections import MultiPoint

from PIL import Image


# Create your models here.

# Model for a user's profile implementing additional field to the user's model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default_profile_image.jpg', upload_to='profile_images')
    bio = models.TextField()
    home_address =  models.TextField(default="")
    phone_number = models.TextField(default="")
    location = geomodels.PointField(default=Point(0.0, 0.0))

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        # Resize image to 100 by 100 size
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

# A model for registering logged in users
class LoggedInUsers(models.Model):
    user = models.ForeignKey( User, on_delete = models.CASCADE )

    def __str__(self):
        return f"User( {self.user.username} )"

# A model used to create a list of user points to be displayed on map
class UserLocationsModel(models.Model):
    user_locations = geomodels.MultiPointField( default = MultiPoint() )

    def __str__(self) -> str:
        return str( self.user_locations )