from importlib.metadata import files
import os
import re
import sys
from controller.case_processing_service import CaseProcessingService

from controller.lab_case_controller import LabCaseController
from model.lab_case import LabCase
from tests.lab_case_controller_test import LabCaseDBMock

test = "C:/Users/User/Dropbox/program/git/lab_project/tests/assets/UD210127_VE_Allele Table_MBL.csv"
name = "UD210127"
case = LabCase(name)
db = LabCaseDBMock()

controller = LabCaseController(db)
controller.register_lab_case(case)
controller.import_allele_table(case, test)

case_processing = CaseProcessingService()
case_processing.check_case_amelogenin_swap(case)
abc = case_processing.set_case_subtype(case)
case_processing.check_swap_trio(case)



csv_folder = input("Insira o diretório do .csv: ")
files_in_folder = os.listdir(csv_folder)
csv_files = []
for file in files_in_folder:
    if re.search(r'.csv$', file):
        csv_files.append(file)

if len(csv_files) != 1:
    if len(csv_files) == 0:
        print("Não foram encontrados arquivos .csv neste diretório.")
    elif len(csv_files) > 1:
        print("Mais de um .csv encontrado neste diretório.")
    print("O programa será fechado")
    sys.exit()

csv_file = csv_files[0]

# ask for main folder
# ask for kit
# walk in main folder searching for all lab cases directories
# get directory names
# from directory names, register in DB
# read case .csv from respective kit
# verify case type
# verify swaps and case subtype

# TODO: calculations
# generate summary table (Case, Type, Log)
# TODO: better log (which locus has inconsistencies?)
# TODO: if exclusion, generate repetition request to secretary (.txt) and print
