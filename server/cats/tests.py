import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Cat, Review, Breed
from users.models import Profile


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture()
def create_breed():
    return Breed.objects.create(title="Test breed")


@pytest.fixture
def create_user():
    return Profile.objects.create_user(username="testuser", password="password123")


@pytest.fixture
def another_user():
    return Profile.objects.create_user(username="anotheruser", password="password456")


@pytest.fixture
def create_cat(create_user, create_breed):
    return Cat.objects.create(
        owner=create_user,
        color="black",
        description="Cute cat",
        age=3,
        breed=create_breed,
    )


@pytest.fixture
def create_review(create_user, create_cat):
    return Review.objects.create(stars=4, owner=create_user, cat=create_cat)


@pytest.mark.django_db
def test_create_cat(api_client, create_user, create_breed):
    api_client.force_authenticate(user=create_user)
    url = reverse("cat-list")
    data = {
        "color": "white",
        "description": "Fluffy cat",
        "age": 2,
        "breed": create_breed.id,
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Cat.objects.filter(color="white").exists()


@pytest.mark.django_db
def test_update_cat(api_client, create_user, create_cat, create_breed):
    api_client.force_authenticate(user=create_user)
    url = reverse("cat-detail", kwargs={"pk": create_cat.id})
    data = {
        "color": "gray",
        "description": "Updated description",
        "age": 5,
        "breed": create_breed.id,
    }

    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK

    create_cat.refresh_from_db()
    assert create_cat.color == "gray"


@pytest.mark.django_db
def test_update_cat_unauthorized(api_client, another_user, create_cat, create_breed):
    api_client.force_authenticate(user=another_user)
    url = reverse("cat-detail", kwargs={"pk": create_cat.id})
    data = {
        "color": "brown",
        "description": "Updated by another user",
        "age": 4,
        "breed": create_breed.id,
    }

    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_cat(api_client, create_user, create_cat):
    api_client.force_authenticate(user=create_user)
    url = reverse("cat-detail", kwargs={"pk": create_cat.id})

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Cat.objects.filter(pk=create_cat.id).exists()


@pytest.mark.django_db
def test_delete_cat_unauthorized(api_client, another_user, create_cat):
    api_client.force_authenticate(user=another_user)
    url = reverse("cat-detail", kwargs={"pk": create_cat.id})

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_review(api_client, create_user, create_cat):
    api_client.force_authenticate(user=create_user)
    review_data = {
        "cat": create_cat.id,
        "stars": 5,
    }

    url = reverse("review-list")

    response = api_client.post(url, review_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Review.objects.count() == 1
    review = Review.objects.first()
    assert review.owner == create_user


@pytest.mark.django_db
def test_update_review(api_client, create_user, create_cat, create_review):
    api_client.force_authenticate(user=create_user)
    updated_data = {
        "cat": create_cat.id,
        "stars": 5,
    }

    url = reverse("review-detail", args=[create_review.id])

    response = api_client.put(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    create_review.refresh_from_db()
    assert create_review.stars == 5


@pytest.mark.django_db
def test_update_review_unauthorized(
    api_client, another_user, create_cat, create_review
):
    api_client.force_authenticate(user=another_user)
    updated_data = {"stars": 2, "cat": create_cat.id}

    url = reverse("review-detail", args=[create_review.id])

    response = api_client.put(url, updated_data, format="json")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_review(api_client, create_user, create_review):
    api_client.force_authenticate(user=create_user)
    url = reverse("review-detail", args=[create_review.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.count() == 0


@pytest.mark.django_db
def test_delete_review_unauthorized(
    api_client, create_user, another_user, create_review
):
    api_client.force_authenticate(user=another_user)
    url = reverse("review-detail", args=[create_review.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert Review.objects.count() == 1
