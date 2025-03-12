from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import get_cart
from .cart_forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect("cart:cart_detail")

@require_POST
def cart_remove(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = get_cart(request)
    return render(request, "shop/cart/detail.html", {
        'cart': cart,
    })

@require_POST
def cart_update(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    if int(request.POST['new_quantity']) <= 0:
        cart.remove(product=product)
        return redirect('cart:cart_detail')
    cart.add(
        product=product,
        quantity=request.POST['new_quantity'],
        override_quantity=True,
    )
    return redirect("cart:cart_detail")

