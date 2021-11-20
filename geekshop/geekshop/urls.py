from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),

    path('admin/', admin.site.urls),
]
