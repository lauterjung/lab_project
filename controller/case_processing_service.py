from controller.lab_case_controller import LabCaseController
from model.genotype import Genotype
from model.lab_case import LabCase, LabCaseSubType, LabCaseType
from model.subject import Gender, Subject, SubjectType 

class CaseProcessingService():
    
    def populate_lab_case(self, lab_case: LabCase):
        lab_case.type_of_case = self.define_type_of_case(lab_case)
        lab_case.amelogenin_swap = self.check_case_amelogenin_swap(lab_case)
        lab_case.subtype_of_case = self.define_case_subtype(lab_case)

    def define_type_of_case(self, case) -> LabCaseType:
        individual_types = []
        for subject in case.subjects:
            individual_types.append(subject.subject_type.name)
                                                            
        if SubjectType.child.name not in individual_types:
            return LabCaseType.invalid
        
        if len(individual_types) == 2:
            if all(x in individual_types for x in [SubjectType.child.name, SubjectType.alledged_father.name]):
                   return LabCaseType.duo

        if len(individual_types) == 2:
            if all(x in individual_types for x in [SubjectType.alledged_mother.name, SubjectType.child.name]):
                   return LabCaseType.maternity_duo
        
        if len(individual_types) == 3: # >= 3, more than 1 child (F1, F2, ...)
            if all(x in individual_types for x in [SubjectType.mother.name, SubjectType.child.name, SubjectType.alledged_father.name]):
                    return LabCaseType.trio

        if len(individual_types) == 3: # >= 3, more than 1 child (F1, F2, ...)
            if all(x in individual_types for x in [SubjectType.alledged_mother.name, SubjectType.child.name, SubjectType.father.name]):
                    return LabCaseType.maternity_trio
        
        return LabCaseType.complex

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
            return result

    # do I need to return a Subject, or only SubjectType/nomenclature/...?
    def check_inconsistencies_two_subjects(self, child_genetic_profile: list[Genotype], subject_1: Subject, subject_2: Subject) -> list[Subject, Subject, int, list[str]]:
        subject_1_genotype = subject_1.get_genetic_profile_as_dictionary()
        subject_2_genotype = subject_2.get_genetic_profile_as_dictionary()

        inconsistencies_locus_list = []
        for genotype in child_genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            subject_1_alleles = [subject_1_genotype[genotype.locus].allele_1, subject_1_genotype[genotype.locus].allele_2]
            subject_2_alleles = [subject_2_genotype[genotype.locus].allele_1, subject_2_genotype[genotype.locus].allele_2]              
           
            if len(set(subject_1_alleles) & set(subject_2_alleles)) == 0:      
                inconsistencies_locus_list.append(genotype.locus)

        # if len(inconsistencies_locus_list) == 0:
        #     return None
        return [subject_1, subject_2, len(inconsistencies_locus_list), inconsistencies_locus_list]
    
    def check_inconsistencies_alledged_parent(self, child_genetic_profile: list[Genotype], known_parent: Subject, child: Subject, alledged_parent: Subject) -> list[Subject, Subject, int, list[str]]:
        known_parent_genotype = known_parent.get_genetic_profile_as_dictionary()
        alledged_parent_genotype = alledged_parent.get_genetic_profile_as_dictionary()
        
        inconsistencies_locus_list = []
        for genotype in child_genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            child_alleles = genotype.allele_1, genotype.allele_2
            known_parent_alleles = [known_parent_genotype[genotype.locus].allele_1, known_parent_genotype[genotype.locus].allele_2]
            alledged_parent_alleles = [alledged_parent_genotype[genotype.locus].allele_1, alledged_parent_genotype[genotype.locus].allele_2]              
         
            if len(set(child_alleles) & set(known_parent_alleles)) == 1 and child_alleles[0] != child_alleles[1]:
                if list(set(child_alleles) - set(known_parent_alleles))[0] not in alledged_parent_alleles:
                    inconsistencies_locus_list.append(genotype.locus)
            elif len(set(child_alleles) & set(alledged_parent_alleles)) == 0:
                   inconsistencies_locus_list.append(genotype.locus)

        # if len(inconsistencies_locus_list) == 0: 
        #     return None
        return [child, alledged_parent, len(inconsistencies_locus_list), inconsistencies_locus_list]    
        
    def OLD_check_inconcistencies_trio(self, lab_case: LabCase) -> list[int]: 
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

        mother_x_alledged_father = []
        mother_x_child = []
        child_x_alledged_father = []
        
        mother_genotype = mother.get_genetic_profile_as_dictionary()
        alledged_father_genotype = alledged_father.get_genetic_profile_as_dictionary()        

        for genotype in child.genetic_profile:
            if genotype.exclude_from_calculations:
                continue

            child_alleles = [genotype.allele_1, genotype.allele_2]
            mother_alleles = [mother_genotype[genotype.locus].allele_1, mother_genotype[genotype.locus].allele_2]
            father_alleles = [alledged_father_genotype[genotype.locus].allele_1, alledged_father_genotype[genotype.locus].allele_2]              

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
        if self.define_type_of_case(lab_case) == LabCaseType.duo or self.define_type_of_case(lab_case) == LabCaseType.complex: # use method or attribute?
            if len(lab_case.amelogenin_swap) > 0:
                return LabCaseSubType.swap
            else:
                return LabCaseSubType.ready
        
        if self.define_type_of_case(lab_case) == LabCaseType.trio:
            if len(lab_case.amelogenin_swap) > 0:
                return LabCaseSubType.swap 
            
            ############# OLD_
            vector = self.OLD_check_inconcistencies_trio(lab_case)

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
    
    def case_to_result_table(self, case: LabCase) -> tuple:
        return(case.name, case.type_of_case.name, case.amelogenin_swap)

    def set_inconsistencies_trio(self, controller: LabCaseController, lab_case: LabCase) -> None: # can i remove controller dependecy?
        result = []
        mother = controller.get_subject_by_type(lab_case, SubjectType.mother)[0]
        children = controller.get_subject_by_type(lab_case, SubjectType.child)
        alledged_father = controller.get_subject_by_type(lab_case, SubjectType.alledged_father)[0]

        if isinstance(children, list):
            result.append(self.check_inconsistencies_two_subjects(children[0].genetic_profile, mother, alledged_father))
        else:
            result.append(self.check_inconsistencies_two_subjects(children.genetic_profile, mother, alledged_father))

        for child in children:
            result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, mother, child))
            result.append(self.check_inconsistencies_alledged_parent(child.genetic_profile, mother, child, alledged_father))
        
        lab_case.inconsistencies = result
        # return [len(mother_x_alledged_father), len(mother_x_child), len(child_x_alledged_father)]    
        pass