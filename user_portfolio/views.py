from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.gis.forms import OSMWidget
from django.contrib.gis.geos import Point
from django.contrib.gis.geos.collections import MultiPoint
from .models import UserLocationsModel

from user_portfolio.models import Profile

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, DisplayUserLocationsForm

def home(request):
    return render(request, 'user_portfolio/home.html')

# Registration Page View
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'user_portfolio/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = self.request.POST['password1']

            user = authenticate(username=username, password=password)
            login(self.request, user)

            messages.success(request, f'Account created for {username}')

            return redirect(to='users-profile')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user_portfolio/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user_portfolio/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


def user_locations(request):
    points_list = [p.location for p in Profile.objects.all()]
    model = UserLocationsModel()
    model.user_locations = MultiPoint( *points_list )
    
    user_locations_form = DisplayUserLocationsForm(instance=model)
    return render(request, 'user_portfolio/user_locations.html', {"user_locations_form": user_locations_form})