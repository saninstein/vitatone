from django.db import models
from sortedm2m.fields import SortedManyToManyField
from django.core.exceptions import ValidationError


class GeneralProduct(models.Model):

    class Meta:
        verbose_name_plural = "Выбор продуктов для главной"
        verbose_name = "Выбор продуктов для главной"

    child = SortedManyToManyField("products.Product", blank=True, verbose_name="Детям", related_name="gen_child")
    adults = SortedManyToManyField("products.Product", blank=True, verbose_name="Взрослым", related_name="gen_adult")
    avitaminoz = SortedManyToManyField("products.Product", blank=True, verbose_name="Авитаминоз", related_name="gen_av")
    hurt = SortedManyToManyField("products.Product", blank=True, verbose_name="Сердце", related_name="gen_hurt")
    beaty = SortedManyToManyField("products.Product", blank=True, verbose_name="Красота", related_name="gen_beaty")



    def __str__(self):
        return "Выбор"

    def clean(self):
        if self._meta.model.objects.count() == 1 and not self.pk:
            raise ValidationError("Может существовать только в одном экземпляре")


class General(models.Model):
    class Meta:
        verbose_name = "  Мета главная"
        verbose_name_plural = "  Мета главная"

    url_ru = "akcia_ru"
    url = "akcia"


    languages = (
        ("ru", "ru"),
        ("uk", "uk"),
        ("en", "en"),
    )

    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    title = models.CharField(max_length=200, verbose_name="Title", blank=True)
    description = models.TextField(max_length=300, verbose_name="Description", blank=True)
    keywords = models.CharField(max_length=300, verbose_name="Keywords", blank=True)

    def __str__(self):
        return self.language

    def clean(self):
        if self._meta.model.objects.count() == 3 and not self.pk:
            raise ValidationError("Может существовать только в одном экземпляре")
        if self._meta.model.objects.filter(language=self.language) and not self.pk:
            raise ValidationError("Уже есть существет с таким языком")