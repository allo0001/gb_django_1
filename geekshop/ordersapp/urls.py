from django.urls import path
from ordersapp import views as ordersapp

app_name = 'orderapp'

urlpatterns = [
    path('', ordersapp.OrderListView.as_view(), name='list'),
    path('create/', ordersapp.OrderCreateView.as_view(), name='create'),
    path('update/<pk>/', ordersapp.OrderUpdateView.as_view(), name='update'),
    path('read/<pk>/', ordersapp.OrderDetailView.as_view(), name='read'),
    path('delete/<pk>/', ordersapp.OrderDeleteView.as_view(), name='delete'),
    path('complete/<pk>/', ordersapp.complite, name='complete'),
]