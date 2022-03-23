import os
import re
import sys
from unittest import result

from controller.case_processing_service import CaseProcessingService
from controller.lab_case_controller import LabCaseController
from model.lab_case import LabCase, LabCaseType
from tests.lab_case_controller_test import LabCaseDBMock

db = LabCaseDBMock()
controller = LabCaseController(db)
case_processing = CaseProcessingService()

analyze_folder = input("Insira o diretório da pasta ANALISAR contendo as pastas raiz dos casos: ")
kit = input("Qual kit está sendo usado?").upper()
case_folders = next(os.walk(analyze_folder+'.'))[1]

result_table = []
for folder_name in case_folders:
    if not re.match(r'.*UD\d{6}', folder_name):
        continue

    case = LabCase(folder_name)
    controller.register_lab_case(case)

    files_in_folder = next(os.walk(analyze_folder+"\\"+folder_name))[2]

    regex_pattern = re.compile(r'.*UD\d{6}.*'+kit+'.*\.csv$')
    csv_files = list(filter(regex_pattern.match, files_in_folder))

    if len(csv_files) != 1:
        if len(csv_files) == 0:
            print("Não foram encontrados arquivos .csv para o caso " + folder_name + " .")
        elif len(csv_files) > 1:
            print("Mais de um .csv encontrado para o caso " + folder_name + " .")
        print("Esse caso será pulado")
        continue

    csv_file = analyze_folder+"\\"+folder_name+"\\"+csv_files[0]
    controller.import_allele_table(case, csv_file)
    case.type_of_case = controller.set_type_of_case(case)

    case_processing.check_case_amelogenin_swap(case)
    
    # abc = case_processing.set_case_subtype(case)
    # case.subtype_of_case = case_processing.set_case_subtype(case)
    
    if case.type_of_case == LabCaseType.trio:
        vector = case_processing.check_swap_trio(case)
        results_swap = ""
        results_mutation_C_AF = ""
        results_mutation_M_C = ""

        if len(case.mother_x_alledged_father) <= 3 or len(case.mother_x_child) > 3:
            results_swap = "TROCA"
        if 0 < len(case.mother_x_child) <= 3:
            results_mutation_M_C = "Mutação entre M e F no(s) loco(s): " + " ".join(case.mother_x_child) + "."
        if 0 < len(case.child_x_alledged_father) <= 3:
            results_mutation_C_AF = "Mutação entre F e SP no(s) loco(s): " + ", ".join(case.child_x_alledged_father) + "."
        inconsistency_list = " ".join([results_swap, results_mutation_M_C, results_mutation_C_AF]).strip()
    else:
        vector = []
        inconsistency_list = []
    
    # result_table.append((case.name, case.type_of_case.name, case.details_amelogenin_swap, vector, inconsistency_list))
    result_table.append((case.name, case.type_of_case.name, case.details_amelogenin_swap, vector, inconsistency_list))
    result_table

### ask for main folder
### ask for kit
### get directory names
### from directory names, register in DB
### read case .csv from respective kit

# verify case type
# verify swaps and case subtype
# TODO: calculations
# generate summary table (Case, Type, Log)
# TODO: better log (which locus has inconsistencies?)
# TODO: if exclusion, generate repetition request to secretary (.txt) and print


# for case in db.lab_cases:
#     for subject in case.subjects:
#         print(subject.name)
#         for genotype in subject.genetic_profile:
#             print(genotype.locus + " " + genotype.allele_1 + " " + genotype.allele_2)