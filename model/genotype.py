from typing import Final


class Genotype:
    exclude_from_calculations: bool

    def __init__(self, kit: str, locus: str, allele_1: str, allele_2: str):
        self.kit = kit
        self.locus = locus
        self.allele_1 = allele_1
        self.allele_2 = allele_2
        self.exclude_from_calculations = self.__set_exclude_from_calc()
    
    def __set_exclude_from_calc(self) -> bool:
        EXCLUDE_FROM_CALC: Final[str] = ["Amel", "Yindel", "DYS391", "DYS576", "DYS570"]
        
        if self.locus in EXCLUDE_FROM_CALC:
            return True
        else:
            return False
