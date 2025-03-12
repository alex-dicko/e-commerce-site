from cart.cart import get_cart

def cart(request):
    cart = get_cart(request)

    return {
        "cart": cart,
    }