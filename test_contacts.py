import unittest
from contacts_manager import valid_phone

class TestContactManager(unittest.TestCase):

    # -------- TEST PHONE VALIDATION --------
    def test_valid_phone_correct(self):
        self.assertTrue(valid_phone("9876543210"))

    def test_valid_phone_less_digits(self):
        self.assertFalse(valid_phone("9876543"))

    def test_valid_phone_more_digits(self):
        self.assertFalse(valid_phone("987654321012"))

    def test_valid_phone_letters(self):
        self.assertFalse(valid_phone("98A6543210"))

    def test_valid_phone_symbols(self):
        self.assertFalse(valid_phone("98765@3210"))

# -------- RUN TESTS --------
if __name__ == '__main__':
    unittest.main()
