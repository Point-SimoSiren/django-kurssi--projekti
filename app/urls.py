from django.urls import path
from .views import landingview, supplierlistview, productlistview

urlpatterns = [
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('products/', productlistview),
]