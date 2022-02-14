from classes.individual import Individual

class LabCase:
        
    def __init__(self, juridicCases: list[str], cardNumbers: list[str],
                 individualM: Individual = None, individualC: Individual = None, individualAF: Individual = None):
        self.juridicCases = juridicCases
        self.cardNumbers = cardNumbers
        self.individualM = individualM
        self.individualC = individualC
        self.individualAF = individualAF

teste = LabCase()
print(teste)