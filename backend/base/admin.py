from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress

modelList = [Product, Review, Order, OrderItem, ShippingAddress]
for item in modelList:
    admin.site.register(item)
