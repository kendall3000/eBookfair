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
        widget=forms.Choice(
            attrs={
                'class': 'btn bg-primary-subtle text-light dropdown-toggle',
                'type': 'button',
                'data-bs-toggle': 'dropdown',
                'aria-expanded': 'false'
            }
        ),
        choices = enumerate([
            "Name",
            "Price, low to high",
            "Price, high to low",
            "In stock, low to high",
            "In stock, high to low"
            ])
    )