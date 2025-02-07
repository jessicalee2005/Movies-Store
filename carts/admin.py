from django.contrib import admin
from .models import Movie, Cart, CartItem, Order

admin.site.register(Movie)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)

