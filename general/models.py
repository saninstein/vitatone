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



