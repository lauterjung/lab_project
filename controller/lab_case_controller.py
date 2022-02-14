from sre_constants import OP_IGNORE
from classes.lab_case import LabCase
from controller.database import LabCaseDB


class LabCaseController:
    
    def register_lab_case(case: LabCase):
        pass

class LabCaseControllerImpl(LabCaseController):
    def __init__(self, db: LabCaseDB):
        self.db = db
        
    def register_lab_case(self, case: LabCase):
        self.db.save(case)