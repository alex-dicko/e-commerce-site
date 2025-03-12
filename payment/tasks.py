from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order

@shared_task
def payment_successful(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = (
        f'Dear {order.first_name}, \n\n'
        f'Your payment was successfull! \n'
        f'Your Order ID is #{order.id}'
    )
    mail_sent = send_mail(
        subject, message, 'admin@myshop.com', [order.email]
    )
    return mail_sent

@shared_task
def payment_refunded(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = (
        f'Dear {order.first_name}, \n\n'
        f'Your payment has been refunded. \n'
        f'{order.get_total_cost} will reach your bank account with in a few days.\n'
        f'Your Order ID is #{order.id}'
    )
    mail_sent = send_mail(
        subject, message, 'admin@myshop.com', [order.email]
    )
    return mail_sent