from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


# Create your tests here.
class ProfileModelTest( TestCase ):
    def test_created_user(self):
        user1 = User.objects.create_user( username="user1" )
        user2 = User.objects.create_user( username="user2" )
        self.assertIs( len( User.objects.all() ) == 2, True )

    def test_automatic_profile_creation(self):
        userObject = User.objects.create_user( username="user3" )
        self.assertIs( len( Profile.objects.filter( user = userObject ) ) == 1, True )

    def test_edit_user_profile(self):
        userObject = User.objects.create_user( username="user" )
        profilesSet = Profile.objects.filter( user = userObject )
        self.assertIs( len( profilesSet ) == 1, True )
        profile = profilesSet.first()
        profile.bio = "Edited"
        profile.save()
        profilesSet = Profile.objects.filter( user = userObject )
        self.assertIs( len( profilesSet ) == 1, True )
        profile2 = profilesSet.first()
        self.assertIs( profile2.bio == "Edited", True )

