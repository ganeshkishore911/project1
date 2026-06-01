from django.urls import path
from .views import CartCreate,CartView,CartUpdate

urlpatterns=[
    path("cartcreate/",CartCreate.as_view(),name="Cartcreate"),
    path("cart/",CartView.as_view(),name="Cartview"),
    path("cart/<uuid:uuid>/",CartUpdate.as_view(),name="cart-delete,update"),
    
]