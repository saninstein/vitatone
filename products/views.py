from django.views.generic import DetailView
from .models import ProductBody


class ProductDetailView(DetailView):
    model = ProductBody
    template_name = "base.html"
