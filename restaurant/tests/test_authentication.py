from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=False)

    def test_user_registration(self):
        data = {
            "username": "newuser",
            "password": "password1236644",
            "email": "newuser@example.com"
        }
        response = self.client.post('/auth/users/', data, format='json')
        print(response.data)  # Print the response to see what's wrong
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')