from django.urls import path
from .views import OrderView,CreateOrder,OrderStats

urlpatterns=[
    path("orders/",OrderView.as_view(),name="orders"),
    path("orders/<int:pk>/",OrderView.as_view(),name="orders-deyails"),
    path("create-order/",CreateOrder.as_view(),name="Orderitemcreate"),
    path("order-stats/",OrderStats.as_view())
    
]