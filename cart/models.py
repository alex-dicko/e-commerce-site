from django.db import models
import uuid
from datetime import datetime, timedelta
from django.utils.timezone import now

# Create your models here.
class UserCart(models.Model):
    session_key = models.UUIDField(primary_key=False, editable=False, default=uuid.uuid4)
    last_updated = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.session_key)
    
    def get_items(self):
        return CartItem.objects.filter(cart=self)
    
    def get_items_amount(self):
        amount = 0
        for item in CartItem.objects.filter(cart=self):
            amount += item.quantity
        return amount
    
    def get_total_price(self):
        price = 0
        for item in self.get_items():
            price += item.product.price * item.quantity
        return price
    
    def add(self, product, quantity=1, override_quantity=False):
        try:
            item = CartItem.objects.get(cart=self, product=product)
        except CartItem.DoesNotExist:
            item = False

        if item:
            if override_quantity:
                difference = int(quantity) - int(item.quantity)  # instead of using original_quantity, use item.quantity
                item.quantity = quantity
                item.save()
                
                # Update stock based on the difference, ensuring we add the difference back
                item.product.stock -= difference
                item.product.save()

            else:
                item.quantity = item.quantity + quantity
                item.save()
                product.stock = product.stock - quantity
                product.save()
        else:
            new_item = CartItem.objects.create(
                cart=self,
                product=product,
                quantity=quantity,
            )
            product.stock = product.stock - quantity
            product.save()
    
    def remove(self, product):
        try:
            item = CartItem.objects.get(cart=self, product=product)
        except CartItem.DoesNotExist:
            pass

        item.product.stock += item.quantity
        item.product.save()
        item.delete()
        
    def clear(self):
        try: 
            CartItem.objects.filter(cart=self).delete()
        except:
            pass

    def save(self, *args, **kwargs):
        self.last_updated = now()
        self.expires = now() + timedelta(hours=3)
        super(UserCart, self).save(*args, **kwargs)
            
class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{str(self.cart.session_key)} - {self.product.name}"
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
