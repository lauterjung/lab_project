from model.lab_case import LabCase
from model.subject import Gender, Subject, SubjectType 

class CaseProcessingService: # do we pass a LabCase here (init) or in the functions/methods?
    def __init__(self) -> None:
        pass
    
    # TODO: maternity trio tests (C, AM, F)
    def check_swap_trio(lab_case: LabCase) -> list[int]:

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
           
        if any(allele not in gf for allele in gm):    
            mother_x_alledged_father_count += 1
        if any(allele not in gc for allele in gm):
            mother_x_child_count += 1
    

        if len([allele for allele in gc if allele in gm]) == 1:
            if [allele for allele in gc if allele not in gm][0] in gf:
                child_x_alledged_father_count += 1
        else:
            if any(allele not in gf for allele in gc):
                child_x_alledged_father_count += 1


        return [mother_x_alledged_father_count, mother_x_child_count, child_x_alledged_father_count]

    def set_case_subtype() -> None:
        # SWAP, MUTATION, RECOGNITION, EXCLUSION
        pass
    
    def check_case_amelogenin_swap(lab_case: LabCase) -> bool:
        if any(subject.check_subject_amelogenin_swap() for subject in lab_case.subjects):
            return True
        else:
            return False