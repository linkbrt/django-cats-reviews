import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Cat, Review
from users.models import Profile


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return Profile.objects.create_user(username='testuser', password='password123')

@pytest.fixture
def create_cat(create_user):
    return Cat.objects.create(owner=create_user, color='black', description='Cute cat', age=3)

@pytest.mark.django_db
def test_create_cat(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    url = reverse('cat-list')  # предполагаем, что используется стандартная маршрутизация
    data = {'color': 'white', 'description': 'Fluffy cat', 'age': 2}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Cat.objects.filter(color='white').exists()

@pytest.mark.django_db
def test_update_cat(api_client, create_user, create_cat):
    api_client.force_authenticate(user=create_user)
    url = reverse('cat-detail', kwargs={'pk': create_cat.id})
    data = {'color': 'gray', 'description': 'Updated description', 'age': 5}
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    create_cat.refresh_from_db()
    assert create_cat.color == 'gray'

@pytest.mark.django_db
def test_update_cat_unauthorized(api_client, create_user, create_cat):
    another_user = Profile.objects.create_user(username='anotheruser', password='password456')
    api_client.force_authenticate(user=another_user)
    url = reverse('cat-detail', kwargs={'pk': create_cat.id})
    data = {'color': 'brown', 'description': 'Updated by another user', 'age': 4}
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_delete_cat(api_client, create_user, create_cat):
    api_client.force_authenticate(user=create_user)
    url = reverse('cat-detail', kwargs={'pk': create_cat.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Cat.objects.filter(pk=create_cat.id).exists()
