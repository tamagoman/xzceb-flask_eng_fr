import unittest

from translator import englishToFrench, frenchToEnglish

class testTranslator(unittest.TestCase):
    def test_english(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_french(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()