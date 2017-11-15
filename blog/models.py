from django.db import models, transaction
from uuslug import uuslug


class Post(models.Model):

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    image = models.ImageField(verbose_name="Картинка", help_text="Выберете картинку")



class PostBody(models.Model):

    class Meta:
        verbose_name = "Текст статьи"
        verbose_name_plural = "Тексты статей"


    languages = (
        ("UA", "UA"),
        ("RU", "RU"),
        ("EN", "EN"),
    )

    _slug_length = 100

    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовк")
    text = models.TextField(max_length=5000, verbose_name="Текст", help_text="Введите текст")
    language = models.CharField(max_length=10, choices=languages, default=languages[0][0], verbose_name="Язык")
    slug = models.SlugField(max_length=_slug_length, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self, max_length=self._slug_length)
        super(PostBody, self).save(*args, **kwargs)
