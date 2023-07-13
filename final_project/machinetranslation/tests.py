import unittest


class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        
class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_translation(self):
        english_text = "Bonjour"
        expected_french_text = "Hello"
                

if __name__ == '__main__':
    unittest.main()