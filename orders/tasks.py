from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from datetime import datetime, timedelta
from django.utils.timezone import now

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = (
        f'Dear {order.first_name}, \n\n'
        f'We have receieved your order. \n'
        f'Your Order ID is #{order.id}\n'
        f'Current Status: {order.status}'
    )
    mail_sent = send_mail(
        subject, message, 'admin@myshop.com', [order.email]
    )
    return mail_sent

@shared_task
def remove_pending_orders():
    one_hour_ago = now() - timedelta(hours=1)
    orders = Order.objects.filter(created__lt=one_hour_ago, status='pending')
    orders.delete()