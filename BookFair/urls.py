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
    # Profile signup page
    #path('signup-profile/', views.signup_profile, name='signup_profile'),
    # path('user-profile/', user_profile, name='user_profile'),
    path('login/', views.login.as_view(template_name="BookFair/login.html"), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    # Search page
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Warning: this will not work outside of debug mode!
# See: https://docs.djangoproject.com/en/4.2/howto/static-files/ and https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/