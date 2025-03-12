import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .tasks import payment_successful, payment_refunded
import json

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        if (
                session.mode == 'payment'
                and session.payment_status == 'paid'
            ):
                try:
                    order = Order.objects.get(
                        id=session.client_reference_id
                    )
                except Order.DoesNotExist:
                    return HttpResponse(status=404)
                order.status = "completed"
                order.stripe_id = session.payment_intent
                order.save()
                payment_successful.delay(order.id)
    if event.type == 'charge.refunded':
        session = event.data.object
        try:
            order = Order.objects.get(
                stripe_id=session.payment_intent
            )
        except Order.DoesNotExist:
            return HttpResponse(status=404)
        order.status = "refunded"
        order.save()
        payment_refunded.delay(order.id)
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)