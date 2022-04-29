from django.shortcuts import render
from django.http import HttpResponse

from category.models import Category
from listings.models import Listing
from listings.choices import category_choices, currency_choices


def index(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)[:6]
    categories = Category.objects.all()
    context = {
        'listings': listings,
        'categories': categories,
        'currency_choices': currency_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
