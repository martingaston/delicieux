from django.test import TestCase

# Create your tests here.
class TestTesting(TestCase):
    def test_setup_is_ok(self):
        self.assertEqual(1 + 1, 2)


def test_pytest_test_test_test():
    assert 2 * 2 == 4
