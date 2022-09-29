from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos.point import Point

from PIL import Image


# Create your models here.
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

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

