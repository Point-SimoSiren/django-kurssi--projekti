from django.urls import path
from .views import landingview, supplierlistview, productlistview, addsupplier, addproduct, deletesupplier, deleteproduct, edit_product_get, edit_product_post

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:iidee>/',deletesupplier),
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:iidee>/',deleteproduct),
    path('edit-product-get/<int:iidee>/', edit_product_get),
    path('edit-product-post/<int:iidee>/', edit_product_post),
]