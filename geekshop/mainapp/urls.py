from django.urls import path, include
import mainapp.views as mainapp

app_name = 'products'

urlpatterns = [

    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('<int:pk>/<int:page>/', mainapp.products, name='product_paginate'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]