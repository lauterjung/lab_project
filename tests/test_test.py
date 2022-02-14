import unittest

from classes.person import Person


class NamesTestCase(unittest.TestCase):

    def test_person_str(self):
        testPerson = Person(name = "Miguel", age = 29)
        #self.assertEquals(testPerson.name, "Miguel")
        testBrokenPerson = Person(name = 29, age = 29)
        self.assertEquals(testBrokenPerson.name, 29)


