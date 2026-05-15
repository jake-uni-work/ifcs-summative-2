import unittest

from validation import *

class ValidationTests(unittest.TestCase):
    def test_format_name(self):
        self.assertEqual(format_name("ALICE DOE"), "Alice Doe")
        self.assertEqual(format_name("  bob doe "), "Bob Doe")
    
    def test_character_check(self):
        self.assertTrue(validate_name_characters("Alice"))
        self.assertTrue(validate_name_characters("Bob"))
        self.assertFalse(validate_name_characters("Bob1"))
        self.assertFalse(validate_name_characters("Alice_and_Bob"))
        
    def test_length_check(self):
        self.assertFalse(validate_name_length("A"))
        self.assertFalse(validate_name_length("A" * 51))
        self.assertTrue(validate_name_length("Alice"))