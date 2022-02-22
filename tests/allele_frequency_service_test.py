import unittest
from classes.locus import Locus

from controller.allele_frequency_service import AlleleFrequencyService
from controller.database import LocusDB

class AlleleFrequencyServiceTest(unittest.TestCase):
    
    def test_read_allele_frequency(self):
        locus_1 = Locus("D3S1358")
        locus_1.alleles["1"] = 0.001
        
        locus_2 = Locus("vWA")
        locus_2.alleles["1"] = 0.1
        
        locus_3 = Locus("FGA")
        locus_3.alleles["1"] = 0.2
        locus_3.alleles["2,2"] = 0.5
        
        db = LocusDBMock()
        
        file = "tests/assets/allele_frequency_example.csv"
        service = AlleleFrequencyService(db)
        service.read_allele_frequency(file)
        
        saved_locus_1 = db.fetch(locus_1.name)
        saved_locus_2 = db.fetch(locus_2.name)
        saved_locus_3 = db.fetch(locus_3.name)
        
        # self.assertEquals(saved_locus_1, locus_1)
        # self.assertEquals(saved_locus_2, locus_2)
        # self.assertEquals(saved_locus_3, locus_3)
        
        self.assertEquals(saved_locus_1.alleles["1"], locus_1.alleles["1"])
        self.assertEquals(saved_locus_2.alleles["1"], locus_2.alleles["1"])
        self.assertEquals(saved_locus_3.alleles["1"], locus_3.alleles["1"])
        self.assertEquals(saved_locus_3.alleles["2,2"], locus_3.alleles["2,2"])
        
class LocusDBMock(LocusDB):
    loci: list[Locus]
    
    def __init__(self):
        self.loci = []
    
    def save(self, locus: Locus):
        self.loci.append(locus)
    
    def fetch(self, locus: str) -> Locus:
        for saved_locus in self.loci:
            if(saved_locus.name == locus):
                return saved_locus
        return None
