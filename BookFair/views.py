# Django packages
from django.shortcuts import render, HttpResponse, get_object_or_404
# Model packages
from models.models import Category, Product
# Python packages
import random

# Create your views here.
def home(request):
    # Get 4 random object IDs
    num_products = Product.objects.count()
    rand_product_ids = random.sample(range(1,num_products), 4)
    # Get corresponding product objects
    rand_product_objs = [Product.objects.get(pk=prod_id) for prod_id in rand_product_ids]

    return render(request, "BookFair/home.html", {"featured_products": rand_product_objs})

def category(request, cat_id):
    req_category = get_object_or_404(Category, pk=cat_id)

    cat_products = req_category.product_set.all()

    return render(request, "BookFair/category.html", {"category": req_category, "cat_products": cat_products})

def signup_profile(request):
    return render(request, 'BookFair/signup_profile.html')
