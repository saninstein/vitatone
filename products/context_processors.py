from .models import Akciya


def stock(req):
    try:
       item = Akciya.objects.get(language='ru')
       is_stock = item.is_active
    except Akciya.DoesNotExist:
        is_stock = False
    return {
        'stock': is_stock
    }