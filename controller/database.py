from classes.lab_case import LabCase
from classes.locus import Locus

class LabCaseDB:
    
    def save(case: LabCase):
        pass
    
    def fetch(case: int) -> LabCase:
        pass

    def update(case: LabCase):
        # dar update baseado em chave _id
        pass

class LocusDB:
    
    def save(locus: Locus):
        pass
    
    def fetch(locus: str) -> Locus:
        pass