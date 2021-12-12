from django.shortcuts import render

from authapp.models import ShopUser

from mainapp.models import ProductCategory

from mainapp.models import Product


def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users_list.html', context=context)


def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def categories(request):
    context = {
        'object_list': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/categories_list.html', context=context)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category__pk=pk)
    }
    return render(request, 'adminapp/product_list.html', context=context)


def product_create(request):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_read(request, pk):
    pass
