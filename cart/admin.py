from django.contrib import admin
from .models import UserCart
from .models import CartItem

admin.site.register(UserCart)
admin.site.register(CartItem)

# Register your models here.
