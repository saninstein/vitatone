from django.conf.urls import url
from .views import *
from django.urls.conf import path

app_name = 'products'
urlpatterns = [
    path('multiomega', MultiOmegaDetailView.as_view(), name="multiomega_ru"),
    path('<str:lang>/multiomega', MultiOmegaDetailView.as_view(), name="multiomega"),

    path('multivitamin', MultiVitaminDetailView.as_view(), name="multivitamin_ru"),
    path('<str:lang>/multivitamin', MultiVitaminDetailView.as_view(), name="multivitamin"),

    path('vitaminc', VitaminCDetailView.as_view(), name="vitaminc_ru"),
    path('<str:lang>/vitaminc', VitaminCDetailView.as_view(), name="vitaminc"),

    path('ukachivanie', UkachivanieDetailView.as_view(), name="ukachivanie_ru"),
    path('<str:lang>/ukachivanie', UkachivanieDetailView.as_view(), name="ukachivanie"),

    path('jeleyki', JeleykiDetailView.as_view(), name="jeleyki_ru"),
    path('<str:lang>/jeleyki', JeleykiDetailView.as_view(), name="jeleyki"),

    path('shipuchie', ShipuchieaDetailView.as_view(), name="shipuchie_ru"),
    path('<str:lang>/shipuchie', ShipuchieaDetailView.as_view(), name="shipuchie"),

    path('nabor', NaborDetailView.as_view(), name="nabor_ru"),
    path('<str:lang>/nabor', NaborDetailView.as_view(), name="nabor"),

    path('akcia', AkciaView.as_view(), name="akcia_ru"),
    path('<str:lang>/akcia', AkciaView.as_view(), name="akcia"),

    # general & ajax
    path('ditochkam', DitochkamView.as_view(), name="ditochkam_ru"),
    path('<str:lang>/ditochkam', DitochkamView.as_view(), name="ditochkam"),
    path('list/', list_ajax, name='ajax'),
    path('uk/', GeneralView.as_view(), kwargs={'lang': 'uk'}, name='general_uk'),
    path('en/', GeneralView.as_view(), kwargs={'lang': 'en'}, name='general_en'),
    path('<str:lang>/list/', list_ajax, name='ajax'),
    url(r'^$', GeneralView.as_view(), name='general'),
]