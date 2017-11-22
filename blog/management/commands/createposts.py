from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from blog.models import Post, PostBody
from vitatone.settings import BASE_DIR
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(20):
            post = Post()
            path = os.path.join(BASE_DIR ,'blog/management/commands/res/img.jpg')
            post.image = ImageFile(open(path, 'rb'))
            post.save()

            for l, _ in PostBody.languages:
                post_body = PostBody()
                post_body.name = f"Test Заголовок {l} {i}"
                post_body.text = "Текст"
                post_body.language = l
                post_body.post = post
                post_body.save()

        self.stdout.write(self.style.SUCCESS('Test data created'))