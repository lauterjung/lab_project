import csv
import re

from classes.genotype import Genotype
from classes.lab_case import LabCase
from classes.subject import Subject
from controller.database import LabCaseDB

class LabCaseController:
    
    def register_lab_case(case: LabCase):
        pass

class LabCaseControllerImpl(LabCaseController):
    def __init__(self, db: LabCaseDB):
        self.db = db
          
    def register_lab_case(self, case: LabCase):
        if self.db.fetch(case.case_id) == None:
            self.db.save(case)
        else:
            self.db.update(case)
    
    def import_allele_table(self, case: LabCase, file: str):
        file = "tests/assets/allele_table_example.csv"
        
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lines = []
            for row in csv_reader:
                lines.append(row)
        
        for line in lines[1:]:
            name = line[0].strip()
            kit = re.findall(r"(?<=_)[a-zA-Z0-9]{2}$", name)[0]
            locus = line[1].strip()
            allele_1 = line[2].strip()
            allele_2 = line[3].strip() if line[3].strip() != "" else allele_1 
            genetic_profile = Genotype(kit, locus, allele_1, allele_2)
            
            subject = self.__get_subject(case, name)
            
            if subject != None:
                subject.genetic_profile.append(genetic_profile)
            else:
                case.subjects.append(Subject(name, [genetic_profile]))                    
  
    def __get_subject(self, case, name):
        for subject in case.subjects:
            if subject.name == name:
                return subject
        return None
            
    