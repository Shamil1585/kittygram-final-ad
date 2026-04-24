import unittest

class SimpleMathTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
    
    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)
    
    def test_division(self):
        self.assertEqual(10 / 2, 5)
    
    def test_string_concatenation(self):
        self.assertEqual("kitty" + "gram", "kittygram")

class SimpleLogicTests(unittest.TestCase):
    def test_boolean_true(self):
        self.assertTrue(True)
    
    def test_boolean_false(self):
        self.assertFalse(False)
    
    def test_is_none(self):
        self.assertIsNone(None)
    
    def test_is_not_none(self):
        self.assertIsNotNone("something")

if __name__ == '__main__':
    unittest.main()
