from django.urls import path
from . import views
from .views import signup_profile

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Profile signup page
    path('signup-profile/', signup_profile, name='signup_profile')
]