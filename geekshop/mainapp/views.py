import json
import random

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory

from basketapp.models import Basket


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
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all()
            category_item = {'name': 'Все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category__pk=pk)

        paginator = Paginator(product_list, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'links_menu': links_menu,
            'products': products_paginator,
            'category': category_item,
        }
        return render(request, 'mainapp/products_list.html', context)
    hot_product = get_hot_product()
    context = {
        'title': 'товары',
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk=None):
    links_menu = ProductCategory.objects.all()

    context = {
        'links_menu': links_menu,
        'product': get_object_or_404(Product, pk=pk),
    }
    return render(request,'mainapp/product.html', context)

def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json', encoding='utf-8') as contacts_file:
        context = {
            'title': 'Контакты',
            'contacts': json.load(contacts_file),
        }
    return render(request, 'mainapp/contact.html', context)
