from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.models import Menu
from decimal import Decimal


class MenuAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=False)
        self.menu_item = Menu.objects.create(name="Pasta", description="Delicious pasta", price=9.99, availability=True)

    def test_get_menu_list(self):
        response = self.client.get(reverse('menu-items-list'))  # Adjust 'menu-list' if needed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Pasta')
        


    def test_post_menu_item(self):
        data = {
            'name': 'Burger',
            'description': 'Tasty burger',
            'price': 8.99,
            'availability': True
        }
        response = self.client.post(reverse('menu-items-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(name='Burger').price, Decimal('8.99'))
        

