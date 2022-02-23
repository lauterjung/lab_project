from model.subject import Subject

class LabCase:
    case_id: int
        
    def __init__(self, juridic_cases: list[str], card_numbers: list[str], subjects: list[Subject] = []):
        self.juridic_cases = juridic_cases
        self.card_numbers = card_numbers
        self.subjects = subjects
