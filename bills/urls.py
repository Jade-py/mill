from django.contrib import admin
from django.urls import path
from .views import create_bill, print_bill

urlpatterns = [
    path('create-bill/', create_bill, name='create-bill'),
    path('print-bill/', print_bill, name='print-bill'),
]
