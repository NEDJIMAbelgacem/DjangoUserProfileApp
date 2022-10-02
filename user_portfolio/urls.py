from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, RegisterView, CustomLoginView, profile, ChangePasswordView, user_locations
from user_portfolio.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='user_portfolio/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_portfolio/logout.html'), name='logout'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('user_locations/', user_locations, name="user_locations" ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
