from contextlib import redirect_stdout
from controller.case_processing_service import CaseProcessingService
from controller.database import LabCaseDB
from controller.lab_case_controller import LabCaseController

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
    case_processing.populate_lab_case(controller, case)
    result_table_1.append(case_processing.case_to_result_table(case))
    
result_table_1

# with open('output_1.txt', 'w') as f:
#     with redirect_stdout(f):
#         for line in result_table_1:
#             print(line, sep='\n')