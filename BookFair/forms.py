from django import forms
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

    class Meta:
        model = Customer

# class LoginForm(AuthenticationForm):
    
#     class Meta:
#         model = User
#         fields = AuthenticationForm.Meta.fields