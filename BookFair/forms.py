from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from BookFair.models import Customer

class SearchBoxNav(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-primary-subtle text-emphasis',
                'type': 'search',
                'placeholder': 'Search',
                'aria-label': 'Search'
            }
        )
    )

class SearchBoxFull(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-primary text-emphasis',
                'type': 'search',
                'aria-label': 'Search'
            }
        ),
        label=""
    )
    sort = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'btn bg-primary-subtle text-light dropdown-toggle',
                'type': 'button',
                'data-bs-toggle': 'dropdown',
                'aria-expanded': 'false'
            }
        ),
        choices = [
            ("name", "Name"),
            ("price-lh", "Price, low to high"),
            ("price-hl", "Price, high to low"),
            ("stock-lh", "In stock, low to high"),
            ("stock-hl", "In stock, high to low")
        ],
        label = "Sort by:"
    )

class CustomerSignupForm(forms.Form):
    prefix = "signup"

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text'
            }
        ),
        label = "Username"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password'
            }
        ),
        label = "Password",
        validators = [validate_password]
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password'
            }
        ),
        label = "Retype password",
        validators = [validate_password]
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text'
            }
        ),
        label = "First name",
        max_length = 45
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text'
            }
        ),
        label = "Last name",
        max_length = 45
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'myaddress@example.com'
            }
        ),
        label = "Email",
        validators = [validate_email],
        max_length = 128
    )
    initial_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }
        ),
        label = "Initial",
        max_length = 1
    )
    phone_country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }
        ),
        label = "Country prefix",
        max_length = 3
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }
        ),
        label = "Phone number",
        max_length = 12
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text'
            }
        ),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password'
            }
        ),
        label="Password"
    )