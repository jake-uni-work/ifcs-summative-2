import unittest

from screens.end import calculate_categories, determine_count, strongest_and_weakest_categories


class CategoryCalcTest(unittest.TestCase):
    def test_category_count(self):
        self.assertEqual(determine_count(0), 0)
        self.assertEqual(determine_count(1), 0)
        for i in range(2, 4):
            self.assertEqual(determine_count(i), 1)
        for i in range(4, 8):
            self.assertEqual(determine_count(i), 2)
        for i in range(8, 30):
            self.assertEqual(determine_count(i), 3)

    def test_strongest_and_weakeast(self):
            
        scores = {
            "Test1": 1,
            "Test2": 5,
            "Test3": 4,
            "Test4": 2,
            "Test5": 6,
            "Test6": 7,
            "Test7": 3,
            "Test8": 0,
        }
            
        strongest, weakest = strongest_and_weakest_categories(scores)
        
        self.assertEqual(weakest, ["Test8", "Test1", "Test4"])
        self.assertEqual(strongest, ["Test6", "Test5", "Test2"])
