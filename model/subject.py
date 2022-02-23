import re

from model.genotype import Genotype

class Subject():
    type: str
    
    def __init__(self, name: str, genetic_profile: list[Genotype]):
        self.name = name
        self.genetic_profile = genetic_profile 
        self.__set_subject_type()
        
    def __set_subject_type(self):
        regex_pattern = r"(?<=UD\d{6})_?[a-zA-Z0-9]+"

        regex_match = re.findall(regex_pattern, self.name)
        self.type = regex_match[0].removeprefix("_")