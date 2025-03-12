from django.urls import path
from . import views
from . import adminviews

app_name = 'orders'

urlpatterns = [
    path("create/", views.order_create, name='order_create'),

    # ADMIN VIEWS
    path("admin/order/<str:order_id>/", adminviews.admin_order_detail, name='admin_order_detail'),
    path("admin/order/<str:order_id>/pdf/", adminviews.admin_order_pdf, name="admin_order_pdf"),
]
