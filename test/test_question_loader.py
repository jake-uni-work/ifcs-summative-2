import unittest
from question_loader import load_questions

class QuestionLoaderTests(unittest.TestCase):
    def test_load_questions(self):
        expected = [
            {
                'question': 'Lorem ipsum',
                'options': {
                    'a': 'Duis nec ante ultrices',
                    'b': 'Volutpat nunc non',
                    'c': 'Nunc posuere laoreet nulla nec consequat',
                    'd': 'Sed erat lacus, porttitor quis massa eu'
                },
                'correct': 'a',
                'category': 'Lorem Ipsum'
            }
        ]
        
        loaded_questions = load_questions("test/test_questions.csv")
        self.assertEqual(expected, loaded_questions)
