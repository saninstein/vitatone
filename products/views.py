from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from blog.models import PostBody
from general.models import GeneralProduct
from .models import *


class MultilangMixin():
    template_names = []

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        template = [name[1] for name in self.template_names if name[0] == lang]
        if len(template):
            return template
        else:
            raise Http404


class ProductMixin(MultilangMixin):

    def get_context_data(self, **kwargs):
        context = super(ProductMixin, self).get_context_data(**kwargs)

        if self.model is not None:
            lang = self.kwargs.get('lang', 'ru')
            context['item'] = get_object_or_404(self.model, language=lang)
        return context


class ProductPostMixin(ProductMixin):

    def get_context_data(self, **kwargs):
        context = super(ProductPostMixin, self).get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        obj = context.get('item')
        if self.model == MultiOmega:
            obj = MultiOmega.objects.get(language='ru')
            context['posts'] = [x.postbody_set.get(language=lang) for x in obj.posts.all()[:3]]
        if self.model == Ditockam:
            obj = Ditockam.objects.get(language='ru')
        context['products'] = [x.productbody_set.get(language=lang) for x in obj.products.all()[:3]]
        return context



class MultiOmegaDetailView(ProductPostMixin, TemplateView):
    model = MultiOmega
    template_names = (
        ('ru', "multiomega/index.html"),
        ('en', "multiomega/index_en.html"),
        ('uk', "multiomega/index_uk.html")
    )


class MultiVitaminDetailView(ProductMixin, TemplateView):
    model = MultiVitamin
    template_names = (
        ('ru', "multivitamin/index.html"),
        ('en', "multivitamin/index_en.html"),
        ('uk', "multivitamin/index_uk.html")
    )


class VitaminCDetailView(ProductMixin, TemplateView):
    model = VitaminC
    template_names = (
        ('ru', "vitaminc/index.html"),
        ('en', "vitaminc/index_en.html"),
        ('uk', "vitaminc/index_uk.html")
    )


class UkachivanieDetailView(ProductMixin, TemplateView):
    model = Ukachivanie
    template_names = (
        ('ru', "ukachivanie/index.html"),
        ('en', "ukachivanie/index_en.html"),
        ('uk', "ukachivanie/index_uk.html")
    )


class JeleykiDetailView(ProductMixin, TemplateView):
    model = Jeleyki
    template_names = (
        ('ru', "jeleyki/index.html"),
        ('en', "jeleyki/index_en.html"),
        ('uk', "jeleyki/index_uk.html")
    )


class ShipuchieaDetailView(ProductMixin, TemplateView):
    model = Shipuchie
    template_names = (
        ('ru', "shipuchie/index.html"),
        ('en', "shipuchie/index_en.html"),
        ('uk', "shipuchie/index_uk.html")
    )


class NaborDetailView(ProductMixin, TemplateView):
    model = Nabor
    template_names = (
        ('ru', "nabor/index.html"),
        ('en', "nabor/index_en.html"),
        ('uk', "nabor/index_uk.html")
    )


class DitochkamView(ProductPostMixin, TemplateView):
    model = Ditockam

    template_names = (
        ('ru', "ditochkam/index.html"),
        ('en', "ditochkam/index_en.html"),
        ('uk', "ditochkam/index_uk.html")
    )


class GeneralView(MultilangMixin, TemplateView):

    template_names = (
        ('ru', "general/index.html"),
        ('en', "general/index_en.html"),
        ('uk', "general/index_uk.html")
    )


class AkciaView(MultilangMixin, TemplateView):

    template_names = (
        ('ru', "akcia/index.html"),
        ('en', "akcia/index_en.html"),
        ('uk', "akcia/index_uk.html")
    )

    def get_context_data(self, **kwargs):
        context = super(AkciaView, self).get_context_data(**kwargs)
        context['link_nabor'] = Nabor.objects.first().link
        context['item'] = get_object_or_404(Akciya, language=self.kwargs.get('lang', 'ru'))
        return context


def list_ajax(req, lang='ru'):
    it = GeneralProduct.objects.first()
    items = it.child, it.adults, it.avitaminoz, it.hurt, it.beaty
    prods = ProductBody.objects.filter(language=lang)
    res = dict()
    for i, item in zip((1, 2, 6, 7, 8), items):
        l = []
        for x in item.all():
            prod = x.productbody_set.get(language=lang)
            d = {
                    "name": f"<span class='vitatone'>VITA<span>TONE</span></span> {prod.name}",
                    "src": x.image.url,
                    "caption": f"<span style='font-size: 1.2em'><span class='vitatone'>VITA<span>TONE</span></span> {prod.name}</span>",
                    "url": prod.get_absolute_url()
                }
            l.append(d)
        res[f'category{i}'] = l
    return JsonResponse(res)



