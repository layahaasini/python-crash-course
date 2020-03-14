import unittest
from question11_3 import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create a new employee instance."""
        self.annabeth = Employee("Annabeth", "Chase", 5000)

    def test_give_default_raise(self):
        """Test that the default raise is added properly."""
        self.annabeth.give_raise()
        self.assertEqual(self.annabeth.salary, 10000)

    def test_give_custom_raise(self):
        """Test that the custom raise is added properly."""
        self.annabeth.give_raise(10000)
        self.assertEqual(self.annabeth.salary, 15000)

unittest.main()