# Django
from django.db import models
from django.core.validators import (
    MaxValueValidator, 
    MinValueValidator,
)

# Local
from auths.models import Client


class Reviews(models.Model):
    """Class for reviews."""

    user = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        related_name='client_review',
        verbose_name='пользователь'
    )
    review = models.TextField(
        verbose_name='отзыв',
        max_length=2000
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='оценка',
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(5)
        ]
    )
    date_created = models.DateTimeField(
        verbose_name='дата отзыва',
        auto_now=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self) -> str:
        return f'{self.user.username} | {self.date_created}'
    
    