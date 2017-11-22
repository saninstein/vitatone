from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
from blog.utils import get_image_path
from uuslug import uuslug


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


class ProductBody(models.Model):

    class Meta:
        verbose_name = "Описание продукта"
        verbose_name_plural = "Описание продуктов"

    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    _slug_length = 100

    name = models.CharField(max_length=100, default="", verbose_name="Заголовок", help_text="Введите заголовк")
    slug = models.SlugField(max_length=_slug_length, default="", unique=True)
    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def is_ru(self):
        return self.language == 'ru'

    def is_en(self):
        return self.language == 'en'

    def is_uk(self):
        return self.language == 'uk'


    def get_absolute_url(self):
        if self.is_ru():
            return reverse("products:product_ru", args=[self.slug])
        else:
            return reverse("products:product", args=[self.language, self.slug])

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, max_length=self._slug_length)
        super(ProductBody, self).save(*args, **kwargs)
