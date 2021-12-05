from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

import json

from authapp.models import ShopUser


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', encoding='UTF-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for cat in categories:
            ProductCategory.objects.create(**cat)

        products = load_from_json('products')
        Product.objects.all().delete()
        for prod in products:
            _cat = ProductCategory.objects.get(name=prod['category'])
            prod['category'] = _cat
            Product.objects.create(**prod)

        shop_admin = ShopUser.objects.create_superuser(username='django', password='geekbrains')
