import json
import random

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory

from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    product_list = Product.objects.all()
    return random.sample(list(product_list), 1)[0]


def get_same_products(hot_product):
    product_list = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)
    return product_list[:3]


def index(request):

    product_list = Product.objects.all()[:4]

    context = {
        'title': 'Магазин',
        'products': product_list,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all()
            category_item = {'name': 'Все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category__pk=pk)

        context = {
            'links_menu': links_menu,
            'products': product_list,
            'category': category_item,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', context)
    hot_product = get_hot_product()
    context = {
        'title': 'товары',
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json', encoding='utf-8') as contacts_file:
        context = {
            'title': 'Контакты',
            'contacts': json.load(contacts_file),
            'basket': get_basket(request.user),
        }
    return render(request, 'mainapp/contact.html', context)
