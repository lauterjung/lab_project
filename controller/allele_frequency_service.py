from controller.database import LocusDB


class AlleleFrequencyService:
    def __init__(self, db: LocusDB):
        self.db = db
        
    def read_allele_frequency(self, file):
        pass
        # for line in lines[1:]:
        #     name = line[0].strip()
        #     kit = name[-2:]
        #     locus = line[1].strip()
        #     allele_1 = line[2].strip()
        #     allele_2 = line[3].strip() if line[3].strip() != "" else allele_1 
        #     genetic_profile = Genotype(kit, locus, allele_1, allele_2)
            
        #     subject = self.__get_subject(case, name)
            
        #     if subject != None:
        #         subject.genetic_profile.append(genetic_profile)
        #     else:
        #         case.subjects.append(Subject(name, [genetic_profile]))    