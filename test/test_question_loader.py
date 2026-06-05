import unittest
from file_handler import load_questions
from validation import validate_question

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

    def test_missing_question(self):
        data = {
            "option_a": "Option A",
            "option_b": "Option B",
            "option_c": "Option C",
            "option_d": "Option D",
            "correct": "a"
        }
        
        with self.assertRaisesRegex(ValueError, "Question is missing the question"):
            validate_question(data)
            
    def test_missing_option_a(self):
        data = {
            "question": "Question",
            "option_b": "Option B",
            "option_c": "Option C",
            "option_d": "Option D",
            "correct": "a"
        }
        
        with self.assertRaisesRegex(ValueError, "Question is missing option A"):
            validate_question(data)
            
    def test_missing_option_b(self):
        data = {
            "question": "Question",
            "option_a": "Option A",
            "option_c": "Option C",
            "option_d": "Option D",
            "correct": "a"
        }
        
        with self.assertRaisesRegex(ValueError, "Question is missing option B"):
            validate_question(data)
            
    def test_missing_option_c(self):
        data = {
            "question": "Question",
            "option_a": "Option A",
            "option_b": "Option B",
            "option_d": "Option D",
            "correct": "a"
        }
        
        with self.assertRaisesRegex(ValueError, "Question is missing option C"):
            validate_question(data)
            
    def test_missing_option_d(self):
        data = {
            "question": "Question",
            "option_a": "Option A",
            "option_b": "Option B",
            "option_c": "Option C",
            "correct": "a"
        }
        
        with self.assertRaisesRegex(ValueError, "Question is missing option D"):
            validate_question(data)
    
    def test_correct_valid(self):
        data = {
            "question": "Question",
            "option_a": "Option A",
            "option_b": "Option B",
            "option_c": "Option C",
            "option_d": "Option D",
            "correct": 1
        }
        with self.assertRaisesRegex(ValueError, "Correct answer must be a, b, c or d"):
            validate_question(data)
        