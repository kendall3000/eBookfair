# Django packages
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Model packages
from BookFair.models import Category, Product,  Cart, UserProfile, CustomUserCreationForm 
# Form packages
from BookFair.forms import SearchBox
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

    cat_products = req_category.product_set

    # Sorting options
    match request.GET.get('sort'):
        case "name":
            cat_products_sorted = cat_products.order_by('prod_name')
        case "price-lh":
            cat_products_sorted = cat_products.order_by('prod_price')
        case "price-hl":
            cat_products_sorted = cat_products.order_by('-prod_price')
        case "stock-lh":
            cat_products_sorted = cat_products.order_by('prod_stock')
        case "stock-hl":
            cat_products_sorted = cat_products.order_by('-prod_stock')
        case _:
            cat_products_sorted = cat_products.order_by('prod_id').all()

    return render(request, "BookFair/category.html", {"category": req_category, "cat_products": cat_products_sorted})

def product(request, prod_id):
    req_product = get_object_or_404(Product, pk=prod_id)

    return render(request, "BookFair/product.html", {"product": req_product})

def add_to_cart(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the user has an existing cart
    if not hasattr(user_profile, 'cart'):
        cart = Cart.objects.create(user_profile=user_profile)
        user_profile.cart = cart
        user_profile.save()

    # Add the product to the cart
    user_profile.cart.products.add(product)
    messages.success(request, 'Product added to cart!')
    return redirect('user_profile')


def view_cart(request):
    user_profile = UserProfile.objects.get(user=request.user)
    cart = user_profile.cart
    cart_products = cart.products.all()
    return render(request, 'BookFair/view_cart.html', {'cart_products': cart_products})

def user_profile(request):
    user = request.user
    return render(request, 'BookFair/user_profile.html', {'user': user})

def signup_profile(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Error creating your account. Please check the provided information.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'BookFair/signup_profile.html', {'form': form})

# Search
def search(request):
    # The search query is to be submitted as a GET request
    search_form = SearchBox()
    # Initialize query, query_results to none
    query = None
    query_results = None

    # Get the query in the GET request
    if request.GET.get('q'):
        # Make a form object and include the data in the request for validation
        search_form = SearchBox(request.GET)
        # Validate
        if search_form.is_valid():
            query = search_form.cleaned_data['q']
            # Separate query into tokens for word-by-word matching -- inspired by https://stackoverflow.com/questions/28278150/mysql-efficient-search-with-partial-word-match-and-relevancy-score-fulltext
            query_tokens = query.split()
            # Separate tokens, where they will be used in the SQL query
            ## Exact matches    "match"
            exact_match_tokens = ["\"" + token + "\"" for token in query_tokens]
            exact_match_input = " ".join(exact_match_tokens)
            ## Partial matches   match*
            partial_match_tokens = [token + "*" for token in query_tokens]
            partial_match_input = " ".join(partial_match_tokens)
            # Craft SQL query
            sql_query = "SELECT * FROM PRODUCT WHERE MATCH (prod_name, prod_descript) AGAINST ('({}) ({})' IN BOOLEAN MODE)".format(partial_match_input, exact_match_input)
            # Perform raw search query for products
            query_results = Product.objects.raw(sql_query)
        else:
            messages.info(request, 'Invalid search form!')
    else:
        messages.error(request, 'No search query given!') # TODO: make a real "invalid search/no search given" page

    return render(request, "BookFair/search.html", {'search_form': search_form, 'search_results': query_results, 'query': query})