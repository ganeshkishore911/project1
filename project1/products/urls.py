from django.urls import path
from .views import ProductCreate,MainCategoryView,ProductList,ProductView,HomeBannerView

urlpatterns = [
    path('productcreate/',ProductCreate.as_view(),name="create_product"),
    path("category/",MainCategoryView.as_view(),name="main-category"),
    path("category/<int:pk>/",MainCategoryView.as_view()),
    path("productlist/<int:id>/",ProductList.as_view(),name="Productlist"),
    path("product/<int:pk>/",ProductView.as_view(),name="productView"),
    path("homebanner/<str:category>/",HomeBannerView.as_view())

]