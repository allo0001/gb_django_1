from django.urls import path, include
import mainapp.views as mainapp

app_name = 'products'

urlpatterns = [

    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),

]