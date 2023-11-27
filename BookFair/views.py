# Django packages
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from django.views.generic.edit import FormView

# Model packages
from BookFair.models import Customer, Category, Product#,  Cart, UserProfile
# Form packages
from BookFair.forms import SearchBoxNav, SearchBoxFull, CustomerSignupForm, LoginForm
# Python packages
import random
from functools import reduce
import operator
# Logger
import logging

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
            cat_products_sorted = cat_products.order_by('prod_name').all()

    return render(request, "BookFair/category.html", {"category": req_category, "cat_products": cat_products_sorted})

def product(request, prod_id):
    req_product = get_object_or_404(Product, pk=prod_id)

    return render(request, "BookFair/product.html", {"product": req_product})

# def add_to_cart(request, prod_id):
#     product = get_object_or_404(Product, pk=prod_id)
#     user_profile = UserProfile.objects.get(user=request.user)

#     # Check if the user has an existing cart
#     if not hasattr(user_profile, 'cart'):
#         cart = Cart.objects.create(user_profile=user_profile)
#         user_profile.cart = cart
#         user_profile.save()

#     # Add the product to the cart
#     user_profile.cart.products.add(product)
#     messages.success(request, 'Product added to cart!')
#     return redirect('user_profile')


# def view_cart(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     cart = user_profile.cart
#     cart_products = cart.products.all()
#     return render(request, 'BookFair/view_cart.html', {'cart_products': cart_products})

# def user_profile(request):
#     user = request.user
#     return render(request, 'BookFair/user_profile.html', {'user': user})

def signup_profile(request):
    # Creating these, to return if form is made nonexistent
    # create_account_form = UserCreationForm()
    # login_account_form = LoginForm()
    # customer_signup_form = CustomerSignupForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # FIXME: test return message
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You've logged in!")
                form = login_account_form = LoginForm()
                return HttpResponseRedirect("/signup-profile/")
            else:
                messages.error(request, "Wrong credentials. Please check your username and password.")

        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     login(request, user)
        #     messages.success(request, 'Account created successfully!')
        #     # Clear out form
        #     form = create_account_form = UserCreationForm()
        #     # Return to original profile page
        #     return HttpResponseRedirect("/signup-profile/")
        else:
            messages.error(request, 'Error creating your account. Please check the provided information.')
    # create_account_form = UserCreationForm()
    login_account_form = LoginForm()
    customer_signup_form = CustomerSignupForm()

    return render(request, 'BookFair/signup_profile.html', { 'login_account_form': login_account_form, 'customer_signup_form': customer_signup_form})
# 'create_account_form': create_account_form,

def profile(request):
    return render(request, 'BookFair/profile.html')

class signup(FormView):
    template_name = "BookFair/signup.html"
    form_class = CustomerSignupForm

    def get_success_url(self):
        return reverse(profile)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # TODO: check that password is the same -- form validation does not help here
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                messages.success(request, "Successfully signed up!")
                return self.form_valid(form)
            else:
                messages.error(request, "Invalid password.")
                return self.form_invalid(form)

        return self.form_invalid(form)

    @transaction.atomic
    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1']
        )
        Customer.objects.create(
            user = user,
            cus_lname = form.cleaned_data['last_name'],
            cus_fname = form.cleaned_data['first_name'],
            cus_initial = form.cleaned_data['initial_name'],
            cus_email = form.cleaned_data['email'],
            cus_phone = form.cleaned_data['phone_number'],
            cus_phone_country = form.cleaned_data['phone_country']
        ).save()

# Login
class login(LoginView):

    form_class = LoginForm
    template_name = "BookFair/login.html"

    def get_success_url(self):
        return reverse(profile)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(request, "Invalid login. Check your username and password.")
            return self.form_invalid(form)


# Search
def search(request):
    # The search query is to be submitted as a GET request
    search_form_full = SearchBoxFull()
    # Initialize query, query_results to none
    query = None
    query_results_sorted = None

    # Get the query in the GET request
    if request.GET.get('q'):
        # Make a form object and include the data in the request for validation
        ## First attempt it with SearchBoxFull (also setting search_form_full to fill it in w/ user value)
        search_form = search_form_full = SearchBoxFull(request.GET)
        ## Check if the form is not valid -- if it isn't, update it to check the nav form submission
        if not search_form.is_valid():
            search_form = SearchBoxNav(request.GET)
        ## Finally, if the form is valid on either try, get its query; if it's not, log an error.
        if search_form.is_valid():
            query = search_form.cleaned_data['q']

            # Separate query into tokens for word-by-word matching -- inspired by https://stackoverflow.com/questions/28278150/mysql-efficient-search-with-partial-word-match-and-relevancy-score-fulltext
            query_tokens = query.split()

            query_results = Product.objects.filter(
                # Q(prod_name__icontains = token)
                reduce(operator.or_, [Q(prod_name__icontains = token) for token in query_tokens])
                |
                reduce(operator.or_, [Q(prod_descript__icontains = token) for token in query_tokens])
                # Q(prod_descript__icontains = query)
            )

            # Sort time
            # Try to get sort -- if it's not in the POST request, just order it by name
            try:
                sort = search_form.cleaned_data['sort']

                match sort:
                    case "name":
                        query_results_sorted = query_results.order_by('prod_name')
                    case "price-lh":
                        query_results_sorted = query_results.order_by('prod_price')
                    case "price-hl":
                        query_results_sorted = query_results.order_by('-prod_price')
                    case "stock-lh":
                        query_results_sorted = query_results.order_by('prod_stock')
                    case "stock-hl":
                        query_results_sorted = query_results.order_by('-prod_stock')
                    case _:
                        query_results_sorted = query_results.order_by('prod_name')
            except KeyError:
                query_results_sorted = query_results.order_by('prod_name')
        else:
            logging.error('Invalid search form!')
    else:
        logging.error('No search query given!') # TODO: make a real "invalid search/no search given" page

    return render(request, "BookFair/search.html", {'search_form': search_form_full, 'search_results': query_results_sorted, 'query': query})