import unittest
from translator import e2f_translator
from translator import f2e_translator

class TestTranslator(unittest.TestCase):

    def test_e2f_translator(self):
        self.assertEqual(e2f_translator('Hello'), 'Bonjour')
        self.assertNotEqual(e2f_translator('Hello'), 'Hello')
    
    def test_f2e_translator(self):
        self.assertEqual(f2e_translator('Bonjour'), 'Hello')
        self.assertNotEqual(f2e_translator('Bonjour'), 'Bonjour')
    
    def test_e2f_translator_is_null(self):
        self.assertIsNotNone(e2f_translator(None))
    
    def test_f2e_translator_is_null(self):
        self.assertIsNotNone(f2e_translator(None))

if __name__ == '__main__':
    unittest.main()
