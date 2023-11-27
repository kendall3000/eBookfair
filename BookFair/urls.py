from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Category page
    path("category/<int:cat_id>/", views.category, name="category"),
    # Product page
    path("product/<int:prod_id>/", views.product, name="product"),

    # path('user-profile/', user_profile, name='user_profile'),
    
    # Login page
    path('login/', views.CustomerLoginView.as_view(template_name="BookFair/login.html"), name='login'),
    # Signup/registration page
    path('signup/', views.SignupView.as_view(), name='signup'),
    # Profile details
    path('profile/', views.profile, name='profile'),
    # Search page
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Warning: this will not work outside of debug mode!
# See: https://docs.djangoproject.com/en/4.2/howto/static-files/ and https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/