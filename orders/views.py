from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created
from cart.cart import get_cart

def order_create(request):
    cart = get_cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart.get_items():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            order_created.delay(order.id)
            request.session['order_id'] = str(order.id) 
            return redirect('payment:process')
            # return render(
            #     request, "shop/orders/order/created.html",
            #     {
            #         'order': order,
            #     }
            # )
    else:
        form = OrderCreateForm()
    
    return render(
        request, 
        "shop/orders/order/create.html",
        {
            "cart": cart,
            "form": form,
        }
    )
