from controller.lab_case_controller import LabCaseController
from model.genotype import Genotype
from model.lab_case import LabCase, LabCaseSubType, LabCaseType
from model.subject import Gender, Kinship, Subject, SubjectType 

class CaseProcessingService():
    
    def populate_lab_case(self, controller, lab_case: LabCase):
        lab_case.type_of_case = self.define_type_of_case(lab_case)
        lab_case.amelogenin_swap = self.check_case_amelogenin_swap(lab_case)
        self.set_inconsistencies(controller, lab_case)
        self.set_inconsistencies_vector(lab_case)
        lab_case.subtype_of_case = self.define_case_subtype(lab_case)
        self.set_inconsistencies_labels(lab_case)

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

            if len(set(child_alleles) & set(mother_alleles)) == 1 and child_alleles[0] != child_alleles[1]:
                if list(set(child_alleles) - set(mother_alleles))[0] not in father_alleles:
                    child_x_alledged_father.append(genotype.locus)
            elif len(set(child_alleles) & set(father_alleles)) == 0:
                   child_x_alledged_father.append(genotype.locus)

        lab_case.mother_x_alledged_father = mother_x_alledged_father
        lab_case.mother_x_child = mother_x_child
        lab_case.child_x_alledged_father = child_x_alledged_father

        return [len(mother_x_alledged_father), len(mother_x_child), len(child_x_alledged_father)]    
    
    def define_case_subtype(self, lab_case: LabCase) -> LabCaseSubType:
        result = []

        if self.define_type_of_case(lab_case) == LabCaseType.invalid:
            result.append(LabCaseSubType.invalid)
            return result

        if len(lab_case.amelogenin_swap) > 0 or lab_case.inconsistencies_vector[0] == 0:
            result.append(LabCaseSubType.swap)
            return result

        if self.define_type_of_case(lab_case) == LabCaseType.complex:
            result.append(LabCaseSubType.complex)
            return result

        if self.define_type_of_case(lab_case) == LabCaseType.trio: # use method or attribute?
            if lab_case.inconsistencies_vector[0] <= 3:
                result.append(LabCaseSubType.potential_swap)
            if 0 < lab_case.inconsistencies_vector[1] <= 3:
                result.append(LabCaseSubType.mutation_known_parent)
        
        if self.define_type_of_case(lab_case) == LabCaseType.trio or \
           self.define_type_of_case(lab_case) == LabCaseType.duo:
            if 0 < lab_case.inconsistencies_vector[2] <= 3:
                result.append(LabCaseSubType.mutation_alledged_parent)
            if lab_case.inconsistencies_vector[2] == 0:
                result.append(LabCaseSubType.inclusion)
            if lab_case.inconsistencies_vector[2] > 3:
                result.append(LabCaseSubType.exclusion)

        return result
    
    def case_to_result_table(self, case: LabCase) -> tuple:
        name = case.name
        type_of_case = case.type_of_case.name
        amelogenin_swap = case.amelogenin_swap if case.amelogenin_swap != [] else " "
        inconsistencies_vector = case.inconsistencies_vector
        inconsistencies_labels = " ".join(case.inconsistencies_labels) if case.inconsistencies_labels != [] else " "
        return(name, type_of_case,amelogenin_swap, inconsistencies_vector, inconsistencies_labels)

    def set_inconsistencies(self, controller: LabCaseController, lab_case: LabCase) -> None: # can i remove controller dependecy?
        result = []

        if lab_case.type_of_case == LabCaseType.trio:
            child = controller.get_subject_by_kinship(lab_case, Kinship.child)[0]
            alledged_parent = controller.get_subject_by_kinship(lab_case, Kinship.alledged_parent)[0]
            known_parent = controller.get_subject_by_kinship(lab_case, Kinship.known_parent)[0]
            result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, known_parent, alledged_parent))
            result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, known_parent, child))
            result.append(self.check_inconsistencies_alledged_parent(child.genetic_profile, known_parent, child, alledged_parent))
        
        if lab_case.type_of_case == LabCaseType.duo:
            child = controller.get_subject_by_kinship(lab_case, Kinship.child)[0]
            alledged_parent = controller.get_subject_by_kinship(lab_case, Kinship.alledged_parent)[0]
            result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, child, alledged_parent))

        lab_case.inconsistencies = result

    def get_inconsistencies_by_kinship_pair(self, case: LabCase, kinship_1: Kinship, kinship_2: Kinship) -> list:
        for inconsistency in case.inconsistencies:
            if (inconsistency[0].kinship == kinship_1 and inconsistency[1].kinship == kinship_2) or \
               (inconsistency[1].kinship == kinship_1 and inconsistency[0].kinship == kinship_2):
                return inconsistency
        return "NA"

    def set_inconsistencies_vector(self, case: LabCase) -> None:
        results = [""] * 3
        inconcistencies_known_parent_alledged_parent = self.get_inconsistencies_by_kinship_pair(case, Kinship.known_parent, Kinship.alledged_parent)
        inconcistencies_known_parent_child = self.get_inconsistencies_by_kinship_pair(case, Kinship.known_parent, Kinship.child)
        inconcistencies_child_alledged_parent = self.get_inconsistencies_by_kinship_pair(case, Kinship.known_parent, Kinship.child)
        
        if isinstance(inconcistencies_known_parent_alledged_parent, list):
            results[0] = inconcistencies_known_parent_alledged_parent[2]
        if isinstance(inconcistencies_known_parent_child, list):
            results[1] = inconcistencies_known_parent_child[2]
        if isinstance(inconcistencies_child_alledged_parent, list):
            results[2] = inconcistencies_child_alledged_parent[2]

        case.inconsistencies_vector = results

    def set_inconsistencies_vector(self, case: LabCase) -> None:
        results = ["NA"] * 3
        for inconsistency in case.inconsistencies:
            if (inconsistency[0].kinship == Kinship.alledged_parent and inconsistency[1].kinship == Kinship.known_parent) or \
               (inconsistency[1].kinship == Kinship.alledged_parent and inconsistency[0].kinship == Kinship.known_parent):
                results[0] = inconsistency[2]
            if (inconsistency[0].kinship == Kinship.child and inconsistency[1].kinship == Kinship.known_parent) or \
               (inconsistency[1].kinship == Kinship.child and inconsistency[0].kinship == Kinship.known_parent):
                results[1] = inconsistency[2]
            if (inconsistency[0].kinship == Kinship.alledged_parent and inconsistency[1].kinship == Kinship.child) or \
               (inconsistency[1].kinship == Kinship.alledged_parent and inconsistency[0].kinship == Kinship.child):
                results[2] = inconsistency[2]
        case.inconsistencies_vector = results
    
    def set_inconsistencies_labels(self, case: LabCase) -> None:
        results = []
        if LabCaseSubType.swap in case.subtype_of_case:
            results.append("TROCA")
        if LabCaseSubType.potential_swap in case.subtype_of_case:
            results.append("POSSÍVEL TROCA")

        if LabCaseSubType.mutation_known_parent in case.subtype_of_case:
            inconsistency = self.get_inconsistencies_by_kinship_pair(case, Kinship.known_parent, Kinship.child)
            results.append("Mutação entre M e F no(s) loco(s): " + " ".join(inconsistency[3]) + ".")
        if LabCaseSubType.mutation_alledged_parent in case.subtype_of_case:
            inconsistency = self.get_inconsistencies_by_kinship_pair(case, Kinship.child, Kinship.alledged_parent)
            results.append("Mutação entre F e SP no(s) loco(s): " + " ".join(inconsistency[3]) + ".")

        case.inconsistencies_labels.extend(results)

    def generate_request(self, case: LabCase) -> None:
        pass
