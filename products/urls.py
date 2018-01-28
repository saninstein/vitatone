from django.conf.urls import url
from .views import *
from django.urls.conf import path

app_name = 'products'
urlpatterns = [
    path('multiomega', MultiOmegaDetailView.as_view(), name="multiomega_ru"),
    path('<str:lang>/multiomega', MultiOmegaDetailView.as_view(), name="multiomega"),
    path('<str:lang>/multiomega.html', LangRedirect.as_view(pattern_name='products:multiomega', permanent=True)),
    path('multiomega.html', RedirectView.as_view(pattern_name='products:multiomega_ru', permanent=True)),

    path('multivitamin', MultiVitaminDetailView.as_view(), name="multivitamin_ru"),
    path('<str:lang>/multivitamin', MultiVitaminDetailView.as_view(), name="multivitamin"),
    path('<str:lang>/multivitamine.html', LangRedirect.as_view(pattern_name='products:multivitamin', permanent=True)),
    path('multivitamine.html', RedirectView.as_view(pattern_name='products:multivitamin_ru', permanent=True)),

    path('vitaminc', VitaminCDetailView.as_view(), name="vitaminc_ru"),
    path('<str:lang>/vitaminc', VitaminCDetailView.as_view(), name="vitaminc"),
    path('<str:lang>/vitamine-c.html', LangRedirect.as_view(pattern_name='products:vitaminc', permanent=True)),
    path('vitamine-c.html', RedirectView.as_view(pattern_name='products:vitaminc_ru', permanent=True)),

    path('ukachivanie', UkachivanieDetailView.as_view(), name="ukachivanie_ru"),
    path('<str:lang>/ukachivanie', UkachivanieDetailView.as_view(), name="ukachivanie"),
    path('<str:lang>/ukachivanie.html', LangRedirect.as_view(pattern_name='products:ukachivanie', permanent=True)),
    path('ukachivanie.html', RedirectView.as_view(pattern_name='products:ukachivanie_ru', permanent=True)),

    path('jeleyki', JeleykiDetailView.as_view(), name="jeleyki_ru"),
    path('<str:lang>/jeleyki', JeleykiDetailView.as_view(), name="jeleyki"),
    path('<str:lang>/jeleyki.html', LangRedirect.as_view(pattern_name='products:jeleyki', permanent=True)),
    path('jeleyki.html', RedirectView.as_view(pattern_name='products:jeleyki_ru', permanent=True)),

    path('shipuchie', ShipuchieaDetailView.as_view(), name="shipuchie_ru"),
    path('<str:lang>/shipuchie', ShipuchieaDetailView.as_view(), name="shipuchie"),
    path('<str:lang>/shipuchie.html', LangRedirect.as_view(pattern_name='products:shipuchie', permanent=True)),
    path('shipuchie.html', RedirectView.as_view(pattern_name='products:shipuchie_ru', permanent=True)),

    path('nabor', NaborDetailView.as_view(), name="nabor_ru"),
    path('<str:lang>/nabor', NaborDetailView.as_view(), name="nabor"),
    path('<str:lang>/nabor.html', LangRedirect.as_view(pattern_name='products:nabor', permanent=True)),
    path('nabor.html', RedirectView.as_view(pattern_name='products:nabor_ru', permanent=True)),

    path('akcia', AkciaView.as_view(), name="akcia_ru"),
    path('<str:lang>/akcia', AkciaView.as_view(), name="akcia"),
    path('<str:lang>/akcia.html', LangRedirect.as_view(pattern_name='products:akcia', permanent=True)),
    path('akcia.html', RedirectView.as_view(pattern_name='products:akcia_ru', permanent=True)),

    # general & ajax
    path('ditochkam', DitochkamView.as_view(), name="ditochkam_ru"),
    path('<str:lang>/ditochkam', DitochkamView.as_view(), name="ditochkam"),
    path('<str:lang>/ditochkam.html', LangRedirect.as_view(pattern_name='products:ditochkam', permanent=True)),
    path('ditochkam.html', RedirectView.as_view(pattern_name='products:ditochkam_ru', permanent=True)),


    path('list/', list_ajax, name='ajax'),
    path('uk/', GeneralView.as_view(), kwargs={'lang': 'uk'}, name='general_uk'),
    path('en/', GeneralView.as_view(), kwargs={'lang': 'en'}, name='general_en'),
    path('uk/index.html', RedirectView.as_view(pattern_name='products:general_uk'), kwargs={'lang': 'uk'}),
    path('en/index.html', RedirectView.as_view(pattern_name='products:general_en'), kwargs={'lang': 'en'}),
    path('<str:lang>/list/', list_ajax, name='ajax'),
    url(r'^$', GeneralView.as_view(), name='general'),
]