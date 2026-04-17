from django.urls import path
from .views import ProductCreate,ProductUpdate,ProductView

urlpatterns = [
    path('productcreate/',ProductCreate.as_view(),name="create_product"),
    path('products/',ProductView.as_view(),name='view-product'),
    path('products/<int:pk>/',ProductView.as_view(),name='view-product'),
    path('product/<int:pk>/',ProductUpdate.as_view(),name="update_product"),
]