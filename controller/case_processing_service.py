from enum import Enum
from controller.lab_case_controller import LabCaseController
from model.lab_case import LabCase, LabCaseSubType, LabCaseType
from model.subject import Gender, Subject, SubjectType 

# TODO: needs to be moved to lab_case

class CaseProcessingService:
    def __init__(self):
        pass
    
    def check_subject_amelogenin_swap(self, subject: Subject) -> bool:
        for genotype in subject.genetic_profile:
            if (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "Y" and subject.gender == Gender.female) or \
               (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "X" and subject.gender == Gender.male):
                subject.amelogenin_swap = True
            else:
                subject.amelogenin_swap = False

    # TODO: maternity trio tests (C, AM, F)
    # TODO: F1 and F2 in the same case. M F1 F2 and SP type is trio or complex?
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

        lab_case.child_x_alledged_father = []
        lab_case.mother_x_alledged_father = []
        lab_case.mother_x_child = []

        mother_genotype = mother.get_genetic_profile_as_dictionary()
        alledged_father_genotype = alledged_father.get_genetic_profile_as_dictionary()        

        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            gc = [genotype.allele_1, genotype.allele_2]
            gm = [mother_genotype[genotype.locus].allele_1, mother_genotype[genotype.locus].allele_2]
            gf = [alledged_father_genotype[genotype.locus].allele_1, alledged_father_genotype[genotype.locus].allele_2]              
           
            if len(set(gf) & set(gm)) == 0:      
                lab_case.mother_x_alledged_father.append(genotype.locus)
            if len(set(gc) & set(gm)) == 0:  
                lab_case.mother_x_child.append(genotype.locus)

            if len(set(gc) & set(gm)) == 1 and gc[0] != gc[1]: #len(set(gc) - set(gm)) != 0:
                if list(set(gc) - set(gm))[0] not in gf:
                    lab_case.child_x_alledged_father.append(genotype.locus)
            elif len(set(gc) & set(gf)) == 0:
                   lab_case.child_x_alledged_father.append(genotype.locus)

        return [len(lab_case.mother_x_alledged_father), len(lab_case.mother_x_child), len(lab_case.child_x_alledged_father)]    
    
    def check_case_amelogenin_swap(self, lab_case: LabCase) -> list[tuple[bool, Subject]]:
        for subject in lab_case.subjects:
            self.check_subject_amelogenin_swap(subject)
            if subject.amelogenin_swap == True:
                lab_case.details_amelogenin_swap.append((True, subject))

    def set_case_subtype(self, lab_case: LabCase) -> LabCaseSubType:
        controller = LabCaseController()
        if controller.set_type_of_case(lab_case) == LabCaseType.duo or controller.set_type_of_case(lab_case) == LabCaseType.complex:         
            if len(lab_case.details_amelogenin_swap) > 0:
                return LabCaseSubType.swap
            else:
                return LabCaseSubType.ready
        
        if controller.set_type_of_case(lab_case) == LabCaseType.trio:
            if len(lab_case.details_amelogenin_swap) > 0:
                return LabCaseSubType.swap 
            
            vector = self.check_swap_trio(lab_case)

            if vector[0] <= 3 or vector[1] > 3:
                return LabCaseSubType.swap
            if 0 < vector[1] <= 3:
                return LabCaseSubType.mutation_mother
            if 0 < vector[2] <= 3:
                return LabCaseSubType.mutation_father
            if vector[2] > 3:
                return LabCaseSubType.exclusion
            if vector[2] == 0:
                return LabCaseSubType.ready