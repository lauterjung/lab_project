
# OP_IGNORE?
from sre_constants import OP_IGNORE

from classes.lab_case import LabCase
from classes.subject import Subject
from controller.database import LabCaseDB

import csv
import re

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
    
    # open file
    # identify subjects
        # subjects = []
        # foreach line 
            # read sample name
            # if sample name not in subjects, append
            # if locus not in genetic_profile, add genotype
    # identify sampletype
        # foreach sample
            # sample_type = regex
            
    file = "tests/assets/allele_table_example.csv"
    csv_file = open(file, "r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0])
  
    # type: SubjectType, name: str, genotype: list[str])
    
    def import_allele_table(self, case: LabCase, file: str):
        file = "tests/assets/allele_table_example.csv"
        # case = LabCase
        
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lines = []
            for row in csv_reader:
                lines.append(row)
        # text edit
        for line in lines:
            if len(line) == 5:
                line.pop() # trailing , ""
            for i, v in enumerate(line):
                line[i] = line[i].strip() # " 16" -> "16"
            if line[3] == "": # homozygote
                line[3] = line[2]
        
        # unique 
        names = []
        subject_r = [] # type, name, genotype
        for line in lines[1:]: # w/o header
            if line[0] not in names:
                names.append(line[0])
        
        regex_pattern = r"(?<=UD\d{6})_?[a-zA-Z0-9]+"
        
        for name in names:
            # name
            s_name = name
            
            # type
            regex_match = re.findall(regex_pattern, name) # ou usar 3rd pt regex
            if regex_match[0].startswith("_"):
                s_type = regex_match[0][1:]
            else:
                s_type = regex_match[0]
        
            case.subjects.append(Subject(type=s_type,name=s_name))
                
        # genotypes = []
        # for line in lines[1:]: # w/o header
        #     if line[1:4] not in genotypes:
        #         genotypes.append(line[1:4])
                
        # subject type
        # https://regexr.com/
        
        
        
        # se der erro no regex?

    # file.close()