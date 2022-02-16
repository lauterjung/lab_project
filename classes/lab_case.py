from classes.individual import Individual

class LabCase:
    
    case_id = int
        
    def __init__(self, juridic_cases: list[str], card_numbers: list[str],
                 individual_m: Individual = None, individual_c: Individual = None, individual_af: Individual = None):
        
        self.juridic_cases = juridic_cases
        self.card_numbers = card_numbers
        self.individual_m = individual_m
        self.individual_c = individual_c
        self.individual_af = individual_af
