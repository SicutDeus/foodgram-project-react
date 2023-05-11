from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='название тега',
        help_text='название тега',
    )
    color = models.CharField(
        max_length=7,
        verbose_name='цвет для тега',
        help_text='цвет для тега',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='идентификатор тега',
        help_text='идентификатор тега',
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
