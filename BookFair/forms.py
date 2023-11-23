from django import forms

class SearchBox(forms.Form):
    search_query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control bg-primary text-emphasis',
                'type': 'search',
                'aria-label': 'Search'
            }
        ),
        label=""
    )