from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.contrib.auth.models import User, AnonymousUser
from .models import Profile, LoggedInUsers
from django.contrib.auth import authenticate, login

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
    
    def test_login_logout_activity(self):
        user1 = User.objects.create_user( username="user1", email="user1@gmail.com", password="password1" )
        user2 = User.objects.create_user( username="user2", email="user2@gmail.com", password="password2" )
        user3 = User.objects.create_user( username="user3", email="user3@gmail.com", password="password3" )

        c1 = Client()
        c2 = Client()
        c3 = Client()
        
        self.assertTrue( c1.login( username='user1', password='password1' ) )
        self.assertTrue( c2.login( username='user2', password='password2' ) )
        self.assertTrue( c3.login( username='user3', password='password3' ) )

        logged_in = LoggedInUsers.objects.all()
        self.assertEqual( len(logged_in), 3 )
        self.assertEqual( set( u.user.username for u in logged_in ), {"user1", "user2", "user3"} )
        
        c2.logout()

        logged_in = LoggedInUsers.objects.all()
        self.assertEqual( len(logged_in), 2 )
        self.assertEqual( set( u.user.username for u in logged_in ), {"user1", "user3"} )


