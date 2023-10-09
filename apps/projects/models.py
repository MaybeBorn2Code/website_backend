# Django
from django.db import models


class Categories(models.Model):
    """Model for categories."""

    title = models.CharField(
        verbose_name='название категории',
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        return self.title


class Images(models.Model):
    """Images for projects."""

    image = models.ImageField(
        verbose_name='изображение',
        upload_to='images/projects/',
        default=''
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class Projects(models.Model):
    """Model for Projects."""

    title = models.CharField(
        verbose_name='название проекта',
        max_length=100,
        unique=True
    )
    description = models.TextField(
        verbose_name='описание проекта',
        max_length=2000,
        null=True,
        blank=True
    )
    link = models.URLField(
        verbose_name='ссылка',
        max_length=500
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE,
        related_name='project_category',
        verbose_name='категория'
    )
    video = models.FileField(
        upload_to='videos/projects/',
        verbose_name='видео',
        default='',
        null=True,
        blank=True
    )
    first_title_image = models.ImageField(
        verbose_name='обязательно титульное изображение',
        upload_to='images/title_images/',
        default='',
        null=False,
        blank=False
    )
    second_title_image = models.ImageField(
        verbose_name='титульное изображение',
        upload_to='images/title_images/',
        default='',
        null=True,
        blank=True
    )
    third_title_image = models.ImageField(
        verbose_name='титульное изображение',
        upload_to='images/title_images/',
        default='',
        null=True,
        blank=True
    )
    images = models.ManyToManyField(
        to=Images,
        verbose_name='изображения',
        blank=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    def __str__(self) -> str:
        return f'{self.title} | {self.category.title}'
