import unittest
from model.locus import Locus

from controller.allele_frequency_service import AlleleFrequencyService
from controller.database import LocusDB

class AlleleFrequencyServiceTest(unittest.TestCase):
    
    def test_read_allele_frequency(self):
        db = LocusDBMock()
        
        file = "tests/assets/allele_frequency_example.csv"
        service = AlleleFrequencyService(db)
        service.read_allele_frequency(file)
        
        locus_1 = Locus("D3S1358")
        locus_1.alleles["1"] = 0.001
        
        locus_2 = Locus("vWA")
        locus_2.alleles["1"] = 0.1
        
        locus_3 = Locus("FGA")
        locus_3.alleles["1"] = 0.2
        locus_3.alleles["2,2"] = 0.5

        locus_4 = Locus("D8S1179")
        locus_4.alleles["1"] = 0.5
        
        saved_locus_1 = db.fetch(locus_1.name)
        saved_locus_2 = db.fetch(locus_2.name)
        saved_locus_3 = db.fetch(locus_3.name)
        saved_locus_4 = db.fetch(locus_4.name)
        
        self.assertEquals(saved_locus_1.alleles["1"], locus_1.alleles["1"])
        self.assertEquals(saved_locus_2.alleles["1"], locus_2.alleles["1"])
        self.assertEquals(saved_locus_3.alleles["1"], locus_3.alleles["1"])
        self.assertEquals(saved_locus_3.alleles["2,2"], locus_3.alleles["2,2"])
        self.assertEquals(saved_locus_4.alleles["1"], locus_4.alleles["1"])
        self.assertEquals(len(db.loci), 4)
    
    
    def test_get_allele_frequency(self):
        allele_name = "1"   
        
        locus = Locus("FGA")
        locus.alleles[allele_name] = 0.2
       
        db = LocusDBMock()
        db.save(locus)
        
        service = AlleleFrequencyService(db)
        allele_frequency = service.get_allele_frequency(locus.name, allele_name)
        
        self.assertEquals(allele_frequency, 0.2)
        
    def test_get_allele_frequency_from_unregistered_item(self):
        allele_name = "1"   
                
        unregistered_locus = Locus("A")
        locus_without_allele = Locus("B")
        
        db = LocusDBMock()
        db.save(locus_without_allele)
        
        service = AlleleFrequencyService(db)
        unregistered_locus_allele_frequency = service.get_allele_frequency(unregistered_locus.name, allele_name)
        unregistered_allele_frequency = service.get_allele_frequency(locus_without_allele.name, allele_name)
        
        self.assertEquals(unregistered_locus_allele_frequency, 0.001)
        self.assertEquals(unregistered_allele_frequency, 0.001)
        
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
