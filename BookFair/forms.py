from django import forms

class SearchBox(forms.Form):
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