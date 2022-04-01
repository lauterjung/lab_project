from model.lab_case import LabCase
from model.locus import Locus

class LabCaseDB:
    lab_cases: list[LabCase]
    
    def __init__(self):
        self.lab_cases = []
    
    def save(self, case: LabCase):
        self.lab_cases.append(case)
        # TODO: if exists
    
    def fetch(self, name: str) -> LabCase:
        for saved_case in self.lab_cases:
            if(saved_case.name == name):
                return saved_case
        return None
    
    def update(self, case: LabCase):
        for i, saved_case in enumerate(self.lab_cases):
            if(saved_case.name == case.name):
                self.lab_cases[i] = case

class LocusDB:
    
    def save(locus: Locus) -> None:
        pass
    
    def fetch(locus: str) -> Locus:
        pass