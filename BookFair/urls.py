from django.urls import path
from . import views
from .views import signup_profile

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Category page
    path("category/<int:cat_id>/", views.category, name="category"),
    # Product page
    path("product/<int:prod_id>/", views.product, name="product"),
    # Profile signup page
    path('signup-profile/', signup_profile, name='signup_profile')
]