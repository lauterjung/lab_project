## case_processing_service.py

# def set_inconsistencies_trio(self, controller: LabCaseController, lab_case: LabCase) -> None: # can i remove controller dependecy?
#     result = []
#     known_parent = controller.get_subject_by_kinship(lab_case, Kinship.known_parent)[0]
#     child = controller.get_subject_by_kinship(lab_case, Kinship.child)[0]
#     alledged_parent = controller.get_subject_by_kinship(lab_case, Kinship.alledged_parent)[0]

#     result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, known_parent, alledged_parent))
#     result.append(self.check_inconsistencies_two_subjects(child.genetic_profile, known_parent, child))
#     result.append(self.check_inconsistencies_alledged_parent(child.genetic_profile, known_parent, child, alledged_parent))
    
#     lab_case.inconsistencies = result

## user_interface.py

# from contextlib import redirect_stdout
# from controller.case_processing_service import CaseProcessingService, SubjectType
# from controller.database import LabCaseDB
# from controller.lab_case_controller import LabCaseController
# from model.lab_case import LabCase, LabCaseType

# db = LabCaseDB()
# controller = LabCaseController(db)
# case_processing = CaseProcessingService()

# # analyze_folder = input("Insira o diretório da pasta ANALISAR contendo as pastas raiz dos casos: ")
# # kit = input("Qual kit está sendo usado? ").upper()
# analyze_folder = r'C:\Users\User\Dropbox\DNA UDESC\ANALISAR'
# kit = "VE"

# result_table_1 = []
# result_table_2 = []

# controller.register_from_folder(analyze_folder)

# for case in db.lab_cases:
#     controller.import_csv_from_folder(case, analyze_folder, kit)

# for case in db.lab_cases:
#     controller.split_lab_case(case)

# db.lab_cases.sort(key = lambda x: x.name)

# for case in db.lab_cases:
#     case_processing.populate_lab_case(case)

#     if case.type_of_case == LabCaseType.trio:
#         vector = case_processing.OLD_check_inconcistencies_trio(case)
#         results_swap = ""
#         results_mutation_C_AF = ""
#         results_mutation_M_C = ""

#         if len(case.mother_x_alledged_father) <= 3 or len(case.mother_x_child) > 3:
#             results_swap = "TROCA"
#         if 0 < len(case.mother_x_child) <= 3:
#             results_mutation_M_C = "Mutação entre M e F no(s) loco(s): " + " ".join(case.mother_x_child) + "."
#         if 0 < len(case.child_x_alledged_father) <= 3:
#             results_mutation_C_AF = "Mutação entre F e SP no(s) loco(s): " + ", ".join(case.child_x_alledged_father) + "."
#         inconsistency_list = " ".join([results_swap, results_mutation_M_C, results_mutation_C_AF]).strip()
#     else:
#         vector = []
#         inconsistency_list = []
    
#     result_table_1.append((case.name, case.type_of_case.name, case.amelogenin_swap, vector))
#     result_table_2.append((case.name, case.type_of_case.name, case.amelogenin_swap, vector, inconsistency_list))
#     result_table_2