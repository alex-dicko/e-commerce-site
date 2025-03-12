from celery import shared_task
from .models import UserCart
from datetime import datetime, timedelta
from django.utils.timezone import now

@shared_task
def remove_expired_carts():
    time_now = now()
    UserCart.objects.filter(expires__lte=time_now).delete()
