import copy
import csv
import os
import re

from model.genotype import Genotype
from model.lab_case import LabCase
from model.subject import Kinship, Subject, SubjectType
from controller.database import LabCaseDB

class LabCaseController():

    cases_to_remove: list

    def __init__(self, db: LabCaseDB):
        self.db = db
        self.kit = None
        self.cases_to_remove = []

    def register_lab_case(self, case: LabCase) -> None:
        if self.db.fetch(case.name) == None:
            self.db.save(case)
        else:
            self.db.update(case)
    
    def delete_lab_case(self, case: LabCase) -> None:
        if self.db.fetch(case.name) != None:
            self.db.delete(case)

    # def split_lab_case(self, case: LabCase) -> None: # maybe there is a better way to do this
    #     children = self.get_subject_by_kinship(case, Kinship.child)
    #     if len(children) <= 1:
    #         return

    #     for child in children:
    #         new_case = LabCase(case.name + child.codification)
    #         for subject in case.subjects:
    #             if subject.kinship != Kinship.child:
    #                 new_case.subjects.append(subject)
    #         new_case.subjects.append(child)
    #         self.db.lab_cases.append(new_case)
    #         del new_case # optional?
    #     self.delete_lab_case(case)

    def split_lab_case(self, case: LabCase) -> None: # maybe there is a better way to do this
        children = self.get_subject_by_kinship(case, Kinship.child)
        alledged_parents = self.get_subject_by_kinship(case, Kinship.alledged_parent)
        if len(children) <= 1 and len(alledged_parents) <= 1:
            return

        for child in children:
            for alledged_parent in alledged_parents:
                
                new_case_name = case.name
                if len(children) > 1:
                    new_case_name = new_case_name + "_" + child.codification
                if len(alledged_parents) > 1:
                    new_case_name = new_case_name + "_" + alledged_parent.codification

                new_case = LabCase(new_case_name)
                new_case.subjects.append(child)
                new_case.subjects.append(alledged_parent)

                for subject in case.subjects:
                    if subject.kinship != Kinship.child and subject.kinship != Kinship.alledged_parent:
                        new_case.subjects.append(subject)

                self.db.lab_cases.append(new_case)
                del new_case # optional?

        self.delete_lab_case(case)

    def remove_pending_cases(self):
        for case in self.cases_to_remove:
            self.delete_lab_case(case)
        
    def import_allele_table(self, case: LabCase, file: str) -> None:
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

    # def __delete_subject(self, case, subject) -> None:
    #     if subject in case.subjects:
    #         self.db.lab_cases.remove(subject)
    #     return None

    def get_subject_by_type(self, case: LabCase, subject_type: SubjectType) -> list[Subject]:
        result = []
        for subject in case.subjects:
            if subject.subject_type == subject_type:
                result.append(subject)
        if len(result) == 0:
            return None
        return result

    def get_subject_by_kinship(self, case: LabCase, kinship: Kinship) -> list[Subject]:
        result = []
        for subject in case.subjects:
            if subject.kinship == kinship:
                result.append(subject)
        return result

    def register_from_folder(self, analyze_folder: str) -> None:
        case_folders = next(os.walk(analyze_folder + '.'))[1]

        for folder_name in case_folders:
            if not re.match(r'.*UD\d{6}$', folder_name):
                continue
            case = LabCase(folder_name)
            self.register_lab_case(case)

    def import_csv_from_folder(self, case: LabCase, analyze_folder: str, kit: str) -> None:
        files_in_folder = next(os.walk(analyze_folder + "\\" + case.name))[2]

        regex_pattern = re.compile(r'.*UD\d{6}.*' + kit + '.*\.csv$')
        csv_files = list(filter(regex_pattern.match, files_in_folder))

        if len(csv_files) != 1:
            if len(csv_files) == 0:
                print("Não foram encontrados arquivos .csv para o caso " + case.name + " .")
            elif len(csv_files) > 1:
                print("Mais de um .csv encontrado para o caso " + case.name + " .")
            print("Esse caso será pulado")
            return

        csv_file = analyze_folder + "\\" + case.name + "\\" + csv_files[0]
        self.import_allele_table(case, csv_file)