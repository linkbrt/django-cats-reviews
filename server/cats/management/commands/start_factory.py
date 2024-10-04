from django.core.management.base import BaseCommand

import factory

from cats.models import Breed, Cat, Review
from users.models import Profile


class Command(BaseCommand):
    help = "Команда, которая создает тестовые данные!"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Создание тестовых данных в БД!"))
        ReviewFactory.create_batch(10)
        self.stdout.write(self.style.SUCCESS("Review"))


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password123")


class BreedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Breed

    title = factory.Faker("word")


class CatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cat

    color = factory.Faker("color_name")
    age = factory.Faker("random_int", min=1, max=120)
    description = factory.Faker("text", max_nb_chars=200)
    owner = factory.SubFactory(UserFactory)
    breed = factory.SubFactory(BreedFactory)


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    stars = factory.Faker("random_int", min=1, max=5)
    cat = factory.SubFactory(CatFactory)
    owner = factory.SubFactory(UserFactory)
