from django.core.management.base import BaseCommand
from blog.models import Post



class Command(BaseCommand):

    def handle(self, *args, **options):
        Post.objects.filter(postbody__name__startswith="Test").delete()
        self.stdout.write(self.style.SUCCESS('Blog is clear'))