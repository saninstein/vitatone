from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='product_ru'),
    path('<str:lang>/<slug:slug>', ProductDetailView.as_view(), name='product')
]