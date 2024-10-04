import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from .models import Profile


@pytest.mark.django_db
def test_create_user_view():
    client = APIClient()
    user_data = {
        "username": "testuser",
        "password": "TestPassword123",
    }
    url = reverse('user-list')

    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

    user = Profile.objects.get(username=user_data['username'])
    assert user.username == user_data['username']
