from django.views.generic import DetailView, ListView
from django.http import Http404
from .models import ProductBody


class ProductDetailView(DetailView):
    model = ProductBody
    template_name = "base.html"


class GeneralView(ListView):
    model = ProductBody
    template_names = (
        ('ru', "general/index.html"),
        ('en', "general/index_en.html"),
        ('uk', "general/index_uk.html")
    )

    context_object_name = "products"

    def get_queryset(self):
        lang = self.kwargs.get('lang', 'ru')
        return self.model.objects.filter(language=lang)

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        template = [name[1] for name in self.template_names if name[0] == lang]
        if len(template):
            return template
        else:
            raise Http404


