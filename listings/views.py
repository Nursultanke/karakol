from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from category.models import Category
from .models import Listing
from django.contrib import messages, auth
from .choices import category_choices, currency_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings, }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    categories = Category.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Category
    if 'category_id' in request.GET:
        category_id = request.GET['category_id']
        if category_id:
            queryset_list = queryset_list.filter(category_id__iexact=category_id)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {'categories': categories, 'listings': queryset_list, 'values': request.GET}
    return render(request, 'listings/search.html', context)


def add_listing(request):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'currency_choices': currency_choices,
        }
        return render(request, 'listings/add_listing.html', context)

    if request.method == 'POST':
        description = request.POST['description']
        title = request.POST['title']
        name = request.POST['name']
        address = request.POST['address']
        price = request.POST['price']
        phone = request.POST['phone']
        whatsapp_phone = request.POST['whatsapp_phone']
        currency = request.POST['currency']
        category_id = request.POST['category']
        # user_id = request.POST['user_id']

        files = request.FILES.getlist('photos')
        print(files)

        new_listing = Listing(description=description, title=title, owner_name=name, address=address, price=price,
                              phone=phone, whatsapp_phone=whatsapp_phone, currency=currency, category_id=category_id)

        try:
            if files[0]:
                new_listing.photo_main = files[0]
                new_listing.save()
        except IndexError:
            pass

        try:
            if files[1]:
                new_listing.photo_1 = files[1]
                new_listing.save()
        except IndexError:
            pass
        try:
            if files[2]:
                new_listing.photo_2 = files[2]
                new_listing.save()
        except IndexError:
            pass

        try:
            if files[3]:
                new_listing.photo_3 = files[3]
                new_listing.save()
        except IndexError:
            pass
        messages.success(request, 'Обьяевление принято')
        return redirect('dashboard')

