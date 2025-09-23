from django.urls import path
from .views import CreateProduct, GetProducts, AddToCart, ViewCart

urlpatterns = [
    path('create/', CreateProduct.as_view(), name='create-product'),
    path('list/', GetProducts.as_view(), name='list-products'),
    path('cart/add/', AddToCart.as_view(), name='add-to-cart'),
    path('cart/view/', ViewCart.as_view(), name='view-cart'),
]