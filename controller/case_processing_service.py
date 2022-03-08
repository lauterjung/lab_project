from model.lab_case import LabCase
from model.subject import Gender, Subject 

class CaseProcessingService: # do we pass a LabCase here (init) or in the functions/methods?
    def __init__(self):
        pass
    
    def check_swap(lab_case: LabCase):
        # foreach subject, verify type and amel genotype
        pass

    def set_case_subtype():
        # SWAP, MUTATION, RECOGNITION, EXCLUSION
        pass
    
    def check_case_amelogenin_swap(lab_case: LabCase) -> bool:
        if any(subject.check_subject_amelogenin_swap() for subject in lab_case.subjects):
            return True
        else:
            return False