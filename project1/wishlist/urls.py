from django.urls import path
from .views import WishlistView,WishlistCreate,WishlistDelete

urlpatterns=[
    path("wishlist/",WishlistView.as_view(),name="Wishlist"),
    path("wishlistcreate/",WishlistCreate.as_view(),name="wishlistcreate"),
    path("wishlist/<int:pk>/",WishlistDelete.as_view()),
    
]