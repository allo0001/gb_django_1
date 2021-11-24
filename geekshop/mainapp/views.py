import json

from django.conf import settings
from django.shortcuts import render


links_menu = [
    {'href': 'home', 'name': 'Дом'},
    {'href': 'modern', 'name': 'Модерн'},
    {'href': 'office', 'name': 'Офис'},
    {'href': 'classic', 'name': 'Классика'},
]


def index(request):
    context = {
        'title': 'Магазин',

    }
    return render(request, 'mainapp/index.html', context)


def products(request, name=None):
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
