from django.urls import path
from . import views
from .views import signup_profile
from .views import category

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Category page
    path("category/<int:cat_id>/", category, name="category")
    # Profile signup page
    path('signup-profile/', signup_profile, name='signup_profile')
]