from model.lab_case import LabCase 

class CaseProcessingService: # do we pass a LabCase here (init) or in the functions/methods?
    def __init__(self):
        pass
    
    def check_swap(self, lab_case: LabCase):
        # foreach subject, verify type and amel genotype
        pass

    def set_case_subtype(self):
        # SWAP, MUTATION, RECOGNITION, EXCLUSION
        pass
    
    def check_amelogenin_swap(self, lab_case: LabCase) -> bool:
        pass
    # if gender male/female, amel