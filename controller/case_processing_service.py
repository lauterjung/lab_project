from controller.lab_case_controller import LabCaseController
from model.genotype import Genotype
from model.lab_case import LabCase, LabCaseSubType, LabCaseType
from model.subject import Gender, Subject, SubjectType 

class CaseProcessingService():
    def __init__(self):
        pass
    
    def check_subject_amelogenin_swap(self, subject: Subject) -> bool:
        for genotype in subject.genetic_profile:
            if (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "Y" and subject.gender == Gender.female) or \
               (genotype.locus == "Amel" and genotype.allele_1 == "X" and genotype.allele_2 == "X" and subject.gender == Gender.male):
                return True
            else:
                return False

    def check_case_amelogenin_swap(self, lab_case: LabCase) -> list[tuple[bool, Subject]]:
        result = []
        for subject in lab_case.subjects:
            if self.check_subject_amelogenin_swap(subject) == True:
                result.append((True, subject))

    def check_inconsistencies_two_subjects(self, lab_case: LabCase, subject_1: Subject, subject_2: Subject) -> list[Subject, Subject, list[str]]:
        subject_1_genotype = subject_1.get_genetic_profile_as_dictionary()
        subject_2_genotype = subject_2.get_genetic_profile_as_dictionary()

        for subject in lab_case.subjects:
            if subject.subject_type.name == SubjectType.child.name:
                child = subject

        inconsistencies_locus_list = []
        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            subject_1_alleles = [subject_1_genotype[genotype.locus].allele_1, subject_1_genotype[genotype.locus].allele_2]
            subject_2_alleles = [subject_2_genotype[genotype.locus].allele_1, subject_2_genotype[genotype.locus].allele_2]              
           
            if len(set(subject_1_alleles) & set(subject_2_alleles)) == 0:      
                inconsistencies_locus_list.append(genotype.locus)

        return [subject_1, subject_2, inconsistencies_locus_list]    
    
    def check_inconsistencies_alledged_parent(self, lab_case: LabCase, known_parent: Subject, child: Subject, alledged_parent: Subject) -> list[Subject, Subject, list[str]]:
        child_genotype = child.get_genetic_profile_as_dictionary()
        known_parent_genotype = known_parent.get_genetic_profile_as_dictionary()
        alledged_parent_genotype = alledged_parent.get_genetic_profile_as_dictionary()
        
        inconsistencies_locus_list = []
        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            child_alleles = [child_genotype[genotype.locus].allele_1, child_genotype[genotype.locus].allele_2]
            known_parent_alleles = [known_parent_genotype[genotype.locus].allele_1, known_parent_genotype[genotype.locus].allele_2]
            alledged_parent_alleles = [alledged_parent_genotype[genotype.locus].allele_1, alledged_parent_genotype[genotype.locus].allele_2]              
         
            if len(set(child_alleles) & set(known_parent_alleles)) == 1 and child_alleles[0] != child_alleles[1]:
                if list(set(child_alleles) - set(known_parent_alleles))[0] not in alledged_parent_alleles:
                    inconsistencies_locus_list.append(genotype.locus)
            elif len(set(child_alleles) & set(alledged_parent_alleles)) == 0:
                   inconsistencies_locus_list.append(genotype.locus)

        return [child, alledged_parent, inconsistencies_locus_list]    

    def check_inconcistencies_trio(self, lab_case: LabCase) -> list[int]: 
        for subject in lab_case.subjects:
            if subject.subject_type.name == SubjectType.child.name:
                child = subject
            elif subject.subject_type.name == SubjectType.mother.name:
                mother = subject
            elif subject.subject_type.name == SubjectType.alledged_father.name:
                alledged_father = subject

        lab_case.child_x_alledged_father = []
        lab_case.mother_x_alledged_father = []
        lab_case.mother_x_child = []

        mother_genotype = mother.get_genetic_profile_as_dictionary()
        alledged_father_genotype = alledged_father.get_genetic_profile_as_dictionary()        

        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            child_alleles = [genotype.allele_1, genotype.allele_2]
            mother_alleles = [mother_genotype[genotype.locus].allele_1, mother_genotype[genotype.locus].allele_2]
            father_alleles = [alledged_father_genotype[genotype.locus].allele_1, alledged_father_genotype[genotype.locus].allele_2]              
            mother_x_alledged_father = []
            mother_x_child = []
            child_x_alledged_father = []

            if len(set(father_alleles) & set(mother_alleles)) == 0:      
                mother_x_alledged_father.append(genotype.locus)
            if len(set(child_alleles) & set(mother_alleles)) == 0:  
                mother_x_child.append(genotype.locus)

            if len(set(child_alleles) & set(mother_alleles)) == 1 and child_alleles[0] != child_alleles[1]: #len(set(child_alleles) - set(mother_alleles)) != 0:
                if list(set(child_alleles) - set(mother_alleles))[0] not in father_alleles:
                    child_x_alledged_father.append(genotype.locus)
            elif len(set(child_alleles) & set(father_alleles)) == 0:
                   child_x_alledged_father.append(genotype.locus)

        lab_case.mother_x_alledged_father = mother_x_alledged_father
        lab_case.mother_x_child = mother_x_child
        lab_case.child_x_alledged_father = child_x_alledged_father

        return [len(mother_x_alledged_father), len(mother_x_child), len(child_x_alledged_father)]    
    
    def define_case_subtype(self, lab_case: LabCase) -> LabCaseSubType:
        controller = LabCaseController()
        if controller.define_type_of_case(lab_case) == LabCaseType.duo or controller.define_type_of_case(lab_case) == LabCaseType.complex:         
            if len(lab_case.details_amelogenin_swap) > 0:
                return LabCaseSubType.swap
            else:
                return LabCaseSubType.ready
        
        if controller.define_type_of_case(lab_case) == LabCaseType.trio:
            if len(lab_case.details_amelogenin_swap) > 0:
                return LabCaseSubType.swap 
            
            vector = self.check_inconcistencies_trio(lab_case)

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