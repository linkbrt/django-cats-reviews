from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Profile


class Cat(models.Model):
    color = models.CharField(verbose_name='Цвет', max_length=50)
    age = models.PositiveIntegerField(verbose_name='Возраст (в месяцах)')
    description = models.TextField(
        verbose_name='Описание', 
        blank=True, null=True
    )
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Котенок'
        verbose_name_plural = 'Котята'


class Review(models.Model):
    stars = models.PositiveIntegerField(
        verbose_name='Звезды',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    cat = models.ForeignKey(to=Cat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
