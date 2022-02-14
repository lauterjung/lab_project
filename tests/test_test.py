import unittest
from classes.lab_case import LabCase

from classes.person import Person


class NamesTestCase(unittest.TestCase):

    def testLabCase(self):
        objLabCase = LabCase(juridicCases=["123456", "789987"], cardNumbers=["123","456"])
        self.assertEqual(["123456", "789987"], objLabCase.juridicCases)
        self.assertIn("123456", objLabCase.juridicCases)
        self.assertIn("456", objLabCase.cardNumbers)
        self.assertNotIn("999", objLabCase.cardNumbers)


# assertEqual
# assertNotEqual
# assertTrue
# assertFalse
# assertIn
# assertNotIn