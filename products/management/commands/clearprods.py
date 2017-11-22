from django.core.management.base import BaseCommand
from products.models import Product



class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.filter(productbody__name__startswith="Test").delete()
        self.stdout.write(self.style.SUCCESS('Prods is clear'))