import unittest
from model.lab_case import LabCase

class NamesTestCase(unittest.TestCase):

    def testLabCase(self):
        objLabCase = LabCase(juridic_cases=["123456", "789987"], card_numbers=["123","456"])
        self.assertEqual(["123456", "789987"], objLabCase.juridic_cases)
        self.assertIn("123456", objLabCase.juridic_cases)
        self.assertIn("456", objLabCase.card_numbers)
        self.assertNotIn("999", objLabCase.card_numbers)


# assertEqual
# assertNotEqual
# assertTrue
# assertFalse
# assertIn
# assertNotIn