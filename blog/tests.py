from django.test import TestCase
from .models import PostBody


class PostBodyTestCase(TestCase):

    def create_postbody(self):
        return PostBody.objects.create(title="Абрка кадабра")

    def test_postbody_slug_length(self):
        postbody = self.create_postbody()
        print(postbody.slug)
        self.assertLessEqual(len(postbody.slug), postbody._slug_length)
