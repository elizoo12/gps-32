"""
modulo de testing de transform.py
"""
import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """clase para probar los metodos de string transforms"""

    def test_is_upper(self):
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")
    """prueba to_upper_case"""

    def test_is_lower(self):
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")
    """prueba to_lower_case"""

    def test_is_capitalize(self):
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")
    """prueba to_capitalize"""


if __name__ == '__main__':
    unittest.main()
