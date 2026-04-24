import unittest
from django.test import TestCase

class SimpleMathTests(TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
    
    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)

class DjangoSetupTest(TestCase):
    def test_django_is_working(self):
        """Test that Django is properly set up"""
        from django.conf import settings
        self.assertTrue(hasattr(settings, 'INSTALLED_APPS'))
    
    def test_apps_are_configured(self):
        """Test that required apps are in INSTALLED_APPS"""
        from django.conf import settings
        self.assertIn('cats', settings.INSTALLED_APPS)

if __name__ == '__main__':
    unittest.main()
