from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from products.models import Product, ProductBody
from vitatone.settings import BASE_DIR
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(20):
            prod = Product()
            path = os.path.join(BASE_DIR ,'products/management/commands/res/img.png')
            prod.image = ImageFile(open(path, 'rb'))
            prod.save()

            for l, _ in ProductBody.languages:
                prod_body = ProductBody()
                prod_body.name = f"Test Продукт {l} {i}"
                prod_body.language = l
                prod_body.product = prod
                prod_body.save()

        self.stdout.write(self.style.SUCCESS('Test data created'))