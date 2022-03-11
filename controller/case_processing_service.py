from model.lab_case import LabCase
from model.subject import Gender, Subject, SubjectType 

class CaseProcessingService:
    def __init__(self):
        pass
    
    def check_subject_amelogenin_swap(self, subject: Subject) -> bool:
        for genotype in subject.genetic_profile:
            if (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "Y" and subject.gender == Gender.female) or \
               (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "X" and subject.gender == Gender.male):
                return True
            else:
                return False

    # TODO: maternity trio tests (C, AM, F)
    def check_swap_trio(self, lab_case: LabCase) -> list[int]:

        for subject in lab_case.subjects:
            if subject.subject_type.name == SubjectType.child.name:
                child = subject
            elif subject.subject_type.name == SubjectType.mother.name:
                mother = subject
            elif subject.subject_type.name == SubjectType.alledged_father.name:
                alledged_father = subject
            # elif subject.subject_type.name == SubjectType.father.name:
            #     father = subject
            # elif subject.subject_type.name == SubjectType.alledged_mother.name:
            #     alledged_mother = subject

        child_x_alledged_father_count = 0
        mother_x_alledged_father_count = 0
        mother_x_child_count = 0
        mother_genotype = mother.get_genetic_profile_as_dictionary()
        alledged_father_genotype = alledged_father.get_genetic_profile_as_dictionary()        

        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            gc = [genotype.allele_1, genotype.allele_2]
            gm = [mother_genotype[genotype.locus].allele_1, mother_genotype[genotype.locus].allele_2]
            gf = [alledged_father_genotype[genotype.locus].allele_1, alledged_father_genotype[genotype.locus].allele_2]              
           
            if len(set(gf) & set(gm)) == 0:      
                mother_x_alledged_father_count += 1
            if len(set(gc) & set(gm)) == 0:  
                mother_x_child_count += 1

            if len(set(gc) & set(gm)) == 1:
                if list(set(gc) - set(gm))[0] not in gf:
                    child_x_alledged_father_count += 1
            elif len(set(gc) & set(gf)) == 0:
                    child_x_alledged_father_count += 1


        return [mother_x_alledged_father_count, mother_x_child_count, child_x_alledged_father_count]

    def set_case_subtype(self) -> None:
        # SWAP, MUTATION, RECOGNITION, EXCLUSION
        pass
    
    def check_case_amelogenin_swap(self, lab_case: LabCase) -> bool:
        if any(self.check_subject_amelogenin_swap(subject) for subject in lab_case.subjects):
            return True
        else:
            return False
