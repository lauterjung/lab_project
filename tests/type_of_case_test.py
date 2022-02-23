import unittest

from model.lab_case import LabCase

class TypeOfCase(unittest.TestCase):

    def test_get_case_type(self):
        juridic_cases = ["12345", "12346"]
        card_numbers = ["123", "456"]
        
        # UD210099
        lab_case_TRIO = LabCase(juridic_cases, card_numbers)
        lab_case_DUO = LabCase(juridic_cases, card_numbers)
        lab_case_COMPLEX = LabCase(juridic_cases, card_numbers)
        
        self.assertEquals(lab_case_TRIO.type_of_case(), "TRIO")
        self.assertEquals(lab_case_DUO.type_of_case(), "DUO")
        self.assertEquals(lab_case_COMPLEX.type_of_case(), "COMPLEX")