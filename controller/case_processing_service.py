from model.lab_case import LabCase
from model.subject import Gender, Subject, SubjectType 

class CaseProcessingService: # do we pass a LabCase here (init) or in the functions/methods?
    def __init__(self) -> None:
        pass
    
    def check_swap_trio(lab_case: LabCase) -> list[int]:
        
        # function get_subject(SubjectType)? 1 vs. 5 loops, performance vs. organization
        # if so, in model\lab_case.py or controller\lab_case_controller.py?
        for subject in lab_case.subjects:
            if subject.subject_type.name == SubjectType.child.name:
                child = subject
            elif subject.subject_type.name == SubjectType.mother.name:
                mother = subject
            elif subject.subject_type.name == SubjectType.father.name:
                father = subject
            elif subject.subject_type.name == SubjectType.alledged_father.name:
                alledged_father = subject
            elif subject.subject_type.name == SubjectType.alledged_mother.name:
                alledged_mother = subject
        
        # TODO: get_genotype

        for genotype in child.genetic_profile:
            if not genotype.exclude_from_calculations:
                gc = child.get_genotype(genotype.locus)
                gm = mother.get_genotype(genotype.locus)
                gf = alledged_father.get_genotype(genotype.locus)
        # loci_names = []
        # for locus in loci_names:        
           
        # return [amelogenin_comparison, child_alledged_father_comparison, mother_alledged_father_comparison, mother_child_comparison]
        pass










    def set_case_subtype() -> None:
        # SWAP, MUTATION, RECOGNITION, EXCLUSION
        pass
    
    def check_case_amelogenin_swap(lab_case: LabCase) -> bool:
        if any(subject.check_subject_amelogenin_swap() for subject in lab_case.subjects):
            return True
        else:
            return False