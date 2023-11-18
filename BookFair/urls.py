from django.urls import path
from . import views
from .views import signup_profile

urlpatterns = [
    path("", views.home, name="home"),
    #path("home", views.home, name="home"),
    path('signup-profile/', signup_profile, name='signup_profile')
]