import shutil
from os import path
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
from blog.utils import get_image_path
from uuslug import uuslug


class Page(models.Model):

    class Meta:
        abstract = True

    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    _slug_length = 100

    name = models.CharField(max_length=100, default="", verbose_name="Название", help_text="Введите Название")
    slug = models.SlugField(max_length=_slug_length, default="", unique=True)
    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")

    title = models.CharField(max_length=200, verbose_name="Title", blank=True)
    description = models.CharField(max_length=300, verbose_name="Description", blank=True)
    keywords = models.CharField(max_length=300, verbose_name="Keywords", blank=True)


    def is_ru(self):
        return self.language == 'ru'

    def is_en(self):
        return self.language == 'en'

    def is_uk(self):
        return self.language == 'uk'

    def __str__(self):
        return self.name

    def get_absolute_url(self, url_ru, url_other):
        if self.is_ru():
            return reverse(f"{url_ru}", args=[self.slug])
        else:
            return reverse(f"{url_other}", args=[self.language, self.slug])


    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, max_length=self._slug_length)
        super(Page, self).save(*args, **kwargs)



class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

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
        return self.productbody_set.first().name

    def save(self, *args, **kwargs):
        if self.pk is None:
            img = self.image
            self.image = None
            super(Product, self).save(*args, **kwargs)
            self.image = img
        super(Product, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Product)
def on_delete_post(sender, instance, using, **kwargs):
    shutil.rmtree(path.dirname(instance.image.path))


class ProductBody(Page):

    class Meta:
        verbose_name = "Описание продукта"
        verbose_name_plural = "Описание продуктов"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return super(ProductBody, self).get_absolute_url(
            "products:product_ru", "products:product"
        )




