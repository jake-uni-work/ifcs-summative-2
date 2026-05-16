import unittest


class SmokeTests(unittest.TestCase):
    def test_smoke(self):
        self.assertTrue(True)
        self.assertEqual(1 + 1, 2)
