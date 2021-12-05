import json

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory

from basketapp.models import Basket


def index(request):

    product_list = Product.objects.all()[:4]

    context = {
        'title': 'Магазин',
        'products': product_list,
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
            'basket': Basket.objects.filter(user=request.user),
        }
        return render(request, 'mainapp/products_list.html', context)

    context = {
        'title': 'товары',
        'links_menu': links_menu,
        'hot_product': Product.objects.all().first(),
        'same_products': Product.objects.all()[:3],
        'basket': Basket.objects.filter(user=request.user),
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contacts.json', encoding='utf-8') as contacts_file:
        context = {
            'title': 'Контакты',
            'contacts': json.load(contacts_file)
        }
    return render(request, 'mainapp/contact.html', context)
