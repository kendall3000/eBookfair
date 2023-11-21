from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import signup_profile, user_profile

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Category page
    path("category/<int:cat_id>/", views.category, name="category"),
    # Product page
    path("product/<int:prod_id>/", views.product, name="product"),
    # Profile signup page
    path('signup-profile/', signup_profile, name='signup_profile'),
    path('user-profile/', user_profile, name='user_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Warning: this will not work outside of debug mode!
# See: https://docs.djangoproject.com/en/4.2/howto/static-files/ and https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/