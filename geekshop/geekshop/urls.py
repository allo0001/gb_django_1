from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.index),
    path('products/', mainapp.products),
    path('contact/', mainapp.contact),

    path('admin/', admin.site.urls),
]
