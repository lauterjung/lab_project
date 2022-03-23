import csv
import re

from model.genotype import Genotype
from model.lab_case import LabCase, LabCaseType
from model.subject import Subject, SubjectType
from controller.database import LabCaseDB

class LabCaseController():
    def __init__(self, db: LabCaseDB):
        self.db = db
          
    def register_lab_case(self, case: LabCase) -> None:
        if self.db.fetch(case.name) == None:
            self.db.save(case)
        else:
            self.db.update(case)
    
    def import_allele_table(self, case: LabCase, file: str) -> None:
        # TODO: case needs to be defined from regex pattern directly from file
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            lines = []
            for row in csv_reader:
                lines.append(row)
        
        for line in lines[1:]:
            name = line[0].strip()
            kit = name[-2:]
            locus = line[1].strip()
            allele_1 = line[2].strip()
            allele_2 = line[3].strip() if line[3].strip() != "" else allele_1 
            genetic_profile = Genotype(kit, locus, allele_1, allele_2)
            
            subject = self.__get_subject(case, name)
            
            if subject != None:
                subject.genetic_profile.append(genetic_profile)
            else:
                case.subjects.append(Subject(name, [genetic_profile]))                    
  
    def __get_subject(self, case, name) -> Subject:
        for subject in case.subjects:
            if subject.name == name:
                return subject
        return None
    
    def set_type_of_case(self, case) -> LabCaseType:
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