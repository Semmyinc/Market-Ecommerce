from django.urls import path
from . import views

urlpatterns = [
    path("payment_success/", views.payment_success, name='payment_success'),
    path("checkout/", views.checkout, name='checkout'),
    path("billing_info/", views.billing_info, name='billing_info'),
    path("process_order/", views.process_order, name='process_order'),
    path("shipped_order/", views.shipped_order, name='shipped_order'),
    path("unshipped_order/", views.unshipped_order, name='unshipped_order'),
    path("all_order/", views.all_order, name='all_order'),
    path("specific_order/<str:pk>/", views.specific_order, name='specific_order'),
]