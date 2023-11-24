# This file should allow for custom "context processors" --
# i.e., a way to consistently get some data across the entire application.

from BookFair.models import Category
from BookFair.forms import SearchBoxNav

def category_list(request):
    categories = Category.objects.all().order_by('cat_id')

    return {'categories_dict': categories}

def searchbox_nav(request):
    search_form_nav = SearchBoxFull()

    return {'search_form_nav': search_form_nav}