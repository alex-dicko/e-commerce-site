from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from orders.models import Order
from cart.cart import get_cart

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        success_url = request.build_absolute_uri(
            reverse("payment:completed", args=[str(order.id)])
        )
        cancel_url = request.build_absolute_uri(
            reverse('payment:cancelled')
        )
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        for item in order.items.all():
            image_url = request.build_absolute_uri(item.product.image.url)
            session_data['line_items'].append(
                {
                    'price_data': {
                        'unit_amount': int(item.price * Decimal('100')), #in pennies for some reason lol, hence x100
                        'currency': 'gbp',
                        'product_data': {
                            'name': item.product.name,
                            'images': [image_url],
                        },
                    },
                    'quantity': item.quantity,
                }
            )
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request, 'shop/payment/process.html', locals())

def payment_completed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    cart = get_cart(request)
    cart.clear()
    if request.session.get('order_id'):
        del request.session['order_id']
    
    return render(request, 'shop/payment/completed.html')
    
        

def payment_cancelled(request):
    return render(request, 'shop/payment/cancelled.html')
