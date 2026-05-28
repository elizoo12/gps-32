"""
modulo de testing de transform.py
"""
import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """clase para probar los metodos de string transforms"""

    def test_is_upper(self):
        """prueba to_upper_case"""
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")


    def test_is_lower(self):
        """prueba to_lower_case"""
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")


    def test_is_capitalize(self):
        """prueba to_capitalize"""
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")



if __name__ == '__main__':
    unittest.main()
