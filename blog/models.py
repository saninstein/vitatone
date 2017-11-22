import shutil
from os import path
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.html import mark_safe
from .utils import get_image_path
from uuslug import uuslug


class Post(models.Model):

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name="Картинка",
        help_text="Выберете картинку"
    )

    def image_tag(self):
        width = self.image.width if self.image.width <= 200 else 200
        print(self.image.path)
        return mark_safe(
            f'<img src={self.image.url} width="{width}px">'
        )

    image_tag.short_description = 'Предпросмотр'

    def name(self):
        return self

    def __str__(self):
        return self.postbody_set.first().title

    def save(self, *args, **kwargs):
        if self.pk is None:
            img = self.image
            self.image = None
            super(Post, self).save(*args, **kwargs)
            self.image = img
        super(Post, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Post)
def on_delete_post(sender, instance, using, **kwargs):
    shutil.rmtree(path.dirname(instance.image.path))


class PostBody(models.Model):

    class Meta:
        verbose_name = "Текст статьи"
        verbose_name_plural = "Тексты статей"

    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    _slug_length = 100

    title = models.CharField(max_length=100, default="", verbose_name="Заголовок", help_text="Введите заголовк")
    text = models.TextField(max_length=5000, default="", verbose_name="Текст", help_text="Введите текст")
    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    slug = models.SlugField(max_length=_slug_length, default="", unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.language == 'ru':
            return reverse("blog:post_ru", args=[self.slug])
        else:
            return reverse("blog:post", args=[self.language, self.slug])

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=self._slug_length)
        super(PostBody, self).save(*args, **kwargs)
