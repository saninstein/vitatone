import shutil
from os import path
from django.db import models
from sortedm2m.fields import SortedManyToManyField
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
from django.utils.html import mark_safe
from .utils import get_image_path
from uuslug import uuslug
from products.models import Page, Product
from django.utils.timezone import now


class PostLink(models.Model):
    _post = models.OneToOneField("blog.Post", on_delete=models.CASCADE)
    def __str__(self):
        return str(self._post)


class Post(models.Model):

    class Meta:
        ordering = ['-id']
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


    image = models.ImageField(
        upload_to=get_image_path,
        verbose_name="Картинка",
        help_text="Выберете картинку"
    )

    image_thumb = models.ImageField(
        upload_to=get_image_path,
        verbose_name="Миниатюра для важно знать",
        help_text="Выберете картинку",
    )

    image_thumb2 = models.ImageField(
        upload_to=get_image_path,
        verbose_name="Миниатюра для списка статей",
        help_text="Выберете картинку",
        blank=True
    )
    date = models.DateField(default=now())
    products = SortedManyToManyField(Product, verbose_name="Продукты")
    posts = SortedManyToManyField(PostLink, verbose_name="Прикреплённые статьи")

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
        return self.postbody_set.filter(language='ru')[0].name

    def save(self, *args, **kwargs):
        if self.pk is None:
            img = self.image
            img_thumb = self.image_thumb
            img_thumb2 = self.image_thumb2
            self.image = None
            super(Post, self).save(*args, **kwargs)
            self.image = img
            self.image_thumb = img_thumb
            self.image_thumb2 = img_thumb2

            link = PostLink()
            link._post = self
            link.save()
        super(Post, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Post)
def on_delete_post(sender, instance, using, **kwargs):
    shutil.rmtree(path.dirname(instance.image.path))


class PostBody(Page):

    class Meta:
        ordering = ['-id']
        verbose_name = "Текст статьи"
        verbose_name_plural = "Тексты статей"

    text = models.TextField(max_length=5000, default="", verbose_name="Текст", help_text="Введите текст")
    mini_text = models.TextField(max_length=240, default="", verbose_name="Текст для 'Ещё советы'", blank=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return super(PostBody, self).get_absolute_url(
            "blog:post_ru", "blog:post"
        )


