class Locus():
    alleles: dict[str, float]
    
    def __init__(self, name: str):
        self.name = name
        self.alleles = {}
        
        
# https://www.w3schools.com/python/python_ref_dictionary.asp