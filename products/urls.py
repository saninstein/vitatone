from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'products'
urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='product_ru'),
    path('<str:lang>/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('<str:lang>', GeneralView.as_view(), name='general'),
    url(r'^$', GeneralView.as_view(), name='general_ru'),
]