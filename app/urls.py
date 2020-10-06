from django.urls import path
from .views import landingview

urlpatterns = [
    path('', landingview),
]