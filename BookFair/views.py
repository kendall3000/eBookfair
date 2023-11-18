from django.shortcuts import render, HttpResponse, get_object_or_404

from models.models import Category, Product

# Create your views here.
def home(request):
    return render(request, "BookFair/home.html")

def category(request, cat_id):
    req_category = get_object_or_404(Category, pk=cat_id)

    return render(request, "BookFair/category.html", {"category": req_category})

def signup_profile(request):
    return render(request, 'BookFair/signup_profile.html')
