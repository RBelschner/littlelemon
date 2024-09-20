from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuModelTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="Pizza", description="Delicious pizza", price=12.99, availability=True)

    def test_menu_creation(self):
        pizza = Menu.objects.get(name="Pizza")
        self.assertEqual(pizza.name, "Pizza")
        self.assertEqual(pizza.price, Decimal('12.99'))
        self.assertEqual(pizza.description, "Delicious pizza")
        self.assertTrue(pizza.availability)
