from django.test import TestCase
from random import sample
from .models import *

class ProductTestCase(TestCase):

    def create_prods(self):
        prod = Product()
        prod.save()
        for i in range(20):
            prod_body = ProductBody()
            prod_body.product = prod
            prod_body.name = f"Test {i}"
            prod_body.save()

    def test_random_choice_products (self):
        ids = ProductBody.objects.values_list('id', flat=True).distinct()
        sample_ids = sample(ids, 3)
        self.assertEqual(sample_ids, 3)
