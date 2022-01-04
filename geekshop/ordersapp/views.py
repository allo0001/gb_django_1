
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView


class OrderListView(ListView):
    pass


class OrderCreateView(CreateView):
    pass


class OrderUpdateView(UpdateView):
    pass


class OrderDeleteView(DeleteView):
    pass


class OrderDetailView(DetailView):
    pass


def complite(request, pk):
    pass


