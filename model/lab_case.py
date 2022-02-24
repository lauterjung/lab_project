from model.subject import Subject

class LabCase:
    id: int
    juridic_cases: list[str]
    card_numbers: list[str]
        
    def __init__(self,  name: str, subjects: list[Subject] = []):
        self.name = name
        self.subjects = subjects

    def type_of_case():
        pass
    # return type_of_case
    # DUO
    # TRIO
    # COMPLEX