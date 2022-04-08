from contextlib import redirect_stdout
from controller.case_processing_service import CaseProcessingService, SubjectType
from controller.database import LabCaseDB
from controller.lab_case_controller import LabCaseController
from model.lab_case import LabCase, LabCaseType

db = LabCaseDB()
controller = LabCaseController(db)
case_processing = CaseProcessingService()

# analyze_folder = input("Insira o diretório da pasta ANALISAR contendo as pastas raiz dos casos: ")
# kit = input("Qual kit está sendo usado? ").upper()
analyze_folder = r'C:\Users\User\Dropbox\DNA UDESC\ANALISAR'
kit = "VE"

result_table_1 = []
result_table_2 = []

controller.register_from_folder(analyze_folder)

for case in db.lab_cases:
    controller.import_csv_from_folder(case, analyze_folder, kit)

for case in db.lab_cases:
    controller.split_lab_case(case)

db.lab_cases.sort(key = lambda x: x.name)

for case in db.lab_cases:
    case_processing.populate_lab_case(case)
    if case.type_of_case == LabCaseType.trio:
        vector = case_processing.OLD_check_inconcistencies_trio(case)
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
    
    result_table_1.append((case.name, case.type_of_case.name, case.amelogenin_swap, vector))
    result_table_2.append((case.name, case.type_of_case.name, case.amelogenin_swap, vector, inconsistency_list))
    result_table_2

# with open('output_1.txt', 'w') as f:
#     with redirect_stdout(f):
#         for line in result_table_1:
#             print(line, sep='\n')

# with open('output_2.txt', 'w') as f:
#     with redirect_stdout(f):
#         for line in result_table_2:
#             print(line, sep='\n')

# for case in db.lab_cases:
#     for subject in case.subjects:
#         print(subject.name)
#         for genotype in subject.genetic_profile:
#             print(genotype.locus + " " + genotype.allele_1 + " " + genotype.allele_2)