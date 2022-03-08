import unittest

from tests.utils.test_setup import TestSetup

class GenotypeTest(unittest.TestCase):
    def setUp(self):
        self.test_setup = TestSetup()

    def test_set_exclude_from_calculations(self):
        self.assertTrue(self.test_setup.male_genotype.exclude_from_calculations())