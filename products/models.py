import shutil
from os import path
from django.forms import ValidationError
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
    description = models.TextField(max_length=300, verbose_name="Description", blank=True)
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
        verbose_name = "Продукт на главной"
        verbose_name_plural = " Продукты на главной"

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
    general_text = models.CharField(max_length=100, verbose_name="Текст для главной", default='')


    def get_absolute_url(self):
        for i in (MultiOmega, MultiVitamin, VitaminC, Ukachivanie, Jeleyki, Shipuchie, Nabor):
            try:
                return i.objects.get(product=self.pk).get_absolute_url()
            except i.DoesNotExist:
                pass
        return "/"



class SingletoneModel(models.Model):

    class Meta:
        abstract = True

    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    url_ru = ""
    url = ""

    product = models.OneToOneField(ProductBody, on_delete=models.PROTECT)
    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    popup = models.TextField(max_length=5000, blank=True, verbose_name="Всплывающее окно")


    def is_ru(self):
        return self.language == 'ru'

    def get_absolute_url(self):
        if self.is_ru():
            return reverse(f"products:{self.url_ru}")
        else:
            return reverse(f"products:{self.url}", args=[self.language])

    def __str__(self):
        return self.language

    def clean(self):
        if self._meta.model.objects.count() == 3 and not self.pk:
            raise ValidationError("Может существовать только в одном экземпляре")
        if self._meta.model.objects.filter(language=self.language) and not self.pk:
            raise ValidationError("Уже есть существет с таким языком")
        if self.language != self.product.language:
            raise ValidationError("Язык не соответствует")


class MultiOmega(SingletoneModel):
    class Meta:
        verbose_name = "МультиОмега"
        verbose_name_plural = "МультиОмега"

    url_ru = "multiomega_ru"
    url = "multiomega"

    text = models.TextField(verbose_name="Текст", blank=True)
    link = models.URLField(verbose_name="Ссылка 'Читать дальше'", blank=True)


class MultiVitamin(SingletoneModel):
    class Meta:
        verbose_name = "Леденцы Мультивитамин"
        verbose_name_plural = "Леденцы Мультивитамин"
    url_ru = "multivitamin_ru"
    url = "multivitamin"


class VitaminC(SingletoneModel):
    class Meta:
        verbose_name = "Леденцы с витамином С"
        verbose_name_plural = "Леденцы с витамином С"
    url_ru = "vitaminc_ru"
    url = "vitaminc"

    text1 = models.TextField(verbose_name="Текст 1", blank=True)
    text2 = models.TextField(verbose_name="Текст 2", blank=True)


class Ukachivanie(SingletoneModel):
    class Meta:
        verbose_name = "Леденцы при укачивании и тошноте"
        verbose_name_plural = "Леденцы при укачивании и тошноте"
    url_ru = "ukachivanie_ru"
    url = "ukachivanie"

    text = models.TextField(verbose_name="Текст", blank=True)


class Jeleyki(SingletoneModel):
    class Meta:
        verbose_name = "Желейные мультивитамины"
        verbose_name_plural = "Желейные мультивитамины"
    url_ru = "jeleyki_ru"
    url = "jeleyki"
    popup = None

    text1 = models.TextField(verbose_name="Текст 1", blank=True)
    text2 = models.TextField(verbose_name="Текст 2", blank=True)


class Shipuchie(SingletoneModel):
    class Meta:
        verbose_name = "Шипучие мультивитамины"
        verbose_name_plural = "Шипучие мультивитамины"
    url_ru = "shipuchie_ru"
    url = "shipuchie"


class Nabor(SingletoneModel):
    class Meta:
        verbose_name = "Подарочный набор"
        verbose_name_plural = "Подарочный набор"
    url_ru = "nabor_ru"
    url = "nabor"
    popup = None

    link = models.URLField(verbose_name="Сслыка на страницу покупки", blank=True)


class Ditockam(models.Model):

    class Meta:
        verbose_name = "Деткам"
        verbose_name_plural = "Деткам"

    url_ru = "ditochkam_ru"
    url = "ditochkam"

    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    title = models.CharField(max_length=200, verbose_name="Title", blank=True)
    description = models.TextField(max_length=300, verbose_name="Description", blank=True)
    keywords = models.CharField(max_length=300, verbose_name="Keywords", blank=True)

    def get_absolute_url(self):
        if self.is_ru():
            return reverse(f"products:{self.url_ru}")
        else:
            return reverse(f"products:{self.url}", args=[self.language])

    def __str__(self):
        return self.language

    def is_ru(self):
        return self.language == 'ru'

    def clean(self):
        if self._meta.model.objects.count() == 3 and not self.pk:
            raise ValidationError("Может существовать только в одном экземпляре")
        if self._meta.model.objects.filter(language=self.language) and not self.pk:
            raise ValidationError("Уже есть существет с таким языком")




