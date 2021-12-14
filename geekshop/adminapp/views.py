from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from authapp.models import ShopUser
from django.urls import reverse
from mainapp.models import ProductCategory, Product

from authapp.form import ShopUserRegisterForm

from adminapp.forms import ShopUserAdminEditForm

from adminapp.forms import ProductCategoryForm

from adminapp.forms import ProductForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users_list.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserRegisterForm()
    context = {
        'form': user_form,
    }
    return render(request, 'adminapp/user_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserAdminEditForm(instance=current_user)
    context = {
        'form': user_form,
    }
    return render(request, 'adminapp/user_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    curent_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        curent_user.is_active = False
        curent_user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        context = {
            'object': curent_user,
        }
        return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    context = {
        'object_list': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/categories_list.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/category_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    current_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES, instance=current_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        form = ProductCategoryForm(instance=current_category)
    context = {
        'form': form,
    }
    return render(request, 'adminapp/category_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    current_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        current_category.is_active = False
        current_category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        context = {
            'object': current_category,
        }
        return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category__pk=pk),
        'category_id': pk,
    }
    return render(request, 'adminapp/product_list.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, category_id):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[category_id]))
    else:
        form = ProductForm()
        context = {
            'form': form,
            'category_id': category_id,
        }
        return render(request, 'adminapp/product_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    category_id = current_product.category.pk
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=current_product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[category_id]))
    else:
        form = ProductForm(instance=current_product)
        context = {
            'form': form,
            'category_id': category_id,
        }
        return render(request, 'adminapp/product_form.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    category_id = current_product.category.pk
    if request.method == 'POST':
        current_product.is_active = False
        current_product.save()
        return HttpResponseRedirect(reverse('adminapp:products', args=[category_id]))
    else:
        form = ProductForm()
        context = {
            'object': current_product,
            'category_id': category_id,
        }
        return render(request, 'adminapp/product_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass
