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
        choices = ["name", "price-lh", "price-hl", "stock-lh", "stock-hl"],
        empty_value = "Sort by"
    )