from django.test import TestCase
from .models import Ingredient

# Create your tests here.
class TestTesting(TestCase):
    def test_setup_is_ok(self):
        self.assertEqual(1 + 1, 2)


def test_pytest_test_test_test():
    assert 2 * 2 == 4


def test_ingredients_model_can_save_data():
    ingredient = Ingredient(name="Chicken")
