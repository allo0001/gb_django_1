import json

from django.conf import settings
from django.shortcuts import render

from mainapp.models import Product, ProductCategory



def index(request):

    product_list = Product.objects.all()[:4]

    context = {
        'title': 'Магазин',
        'products': product_list,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    context = {
        'title': 'товары',
        'links_menu': links_menu,

    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json', encoding='utf-8') as contacts_file:
        context = {
            'title': 'Контакты',
            'contacts': json.load(contacts_file)
        }
    return render(request, 'mainapp/contact.html', context)
