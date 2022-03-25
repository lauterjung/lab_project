from model.lab_case import LabCase
from model.locus import Locus

class LabCaseDB:
    
    def save(case: LabCase) -> None:
        pass
    
    def fetch(case: int) -> LabCase:
        pass

    def update(case: LabCase) -> None:
        # update based on id_key
        pass

class LocusDB:
    
    def save(locus: Locus) -> None:
        pass
    
    def fetch(locus: str) -> Locus:
        pass