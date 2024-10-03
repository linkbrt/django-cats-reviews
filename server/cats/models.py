from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Profile


class Breed(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Cat(models.Model):
    color = models.CharField(verbose_name="Цвет", max_length=50)
    age = models.PositiveIntegerField(verbose_name="Возраст (в месяцах)")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    breed = models.ForeignKey(to=Breed, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.color} : {self.owner.username}"

    class Meta:
        verbose_name = "Котенок"
        verbose_name_plural = "Котята"


class Review(models.Model):
    stars = models.PositiveIntegerField(
        verbose_name="Звезды", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    cat = models.ForeignKey(to=Cat, related_name="reviews", on_delete=models.CASCADE)
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.owner.username} -> {self.stars}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
