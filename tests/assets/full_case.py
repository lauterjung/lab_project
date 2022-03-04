from model.subject import Subject

class FullCaseTest():
    case_name = "UD990000"
    mother_name = case_name+"M"
    child_name = case_name+"F"
    child_2_name = case_name+"F2"
    alledged_father_name = case_name+"SP"
    alledged_mother_name = case_name+"SM"
    father_name = case_name+"P"
    biologic_child_1_name = case_name+"_FB1"
    biologic_child_2_name = case_name+"_FB2"
    auxiliary_mother_1_name = case_name+"_1M"
    auxiliary_mother_2_name = case_name+"_2M"
    auxiliary_father_1_name = case_name+"_1P"
    auxiliary_father_2_name = case_name+"_2P"
    auxiliary_child_1_1_name = case_name+"_1FB1"
    auxiliary_child_1_2_name = case_name+"_1FB2"
    auxiliary_child_2_1_name = case_name+"_2FB1"
    auxiliary_child_2_2_name = case_name+"_2FB2"
    maternal_grandmother_name = case_name+"MM"
    alledged_maternal_grandmother_name = case_name+"SMM"
    maternal_grandfather_name = case_name+"PM"
    alledged_maternal_grandfather_name = case_name+"SPM"
    paternal_grandmother_name = case_name+"MP"
    alledged_paternal_grandmother_name = case_name+"SMP"
    paternal_grandfather_name = case_name+"PP"
    alledged_paternal_grandfather_name = case_name+"SPP"
    maternal_uncle_1_name = case_name+"TM1"
    maternal_uncle_2_name = case_name+"TM2"
    alledged_maternal_uncle_1_name = case_name+"STM1"
    alledged_maternal_uncle_2_name = case_name+"STM2"
    paternal_uncle_1_name = case_name+"TP1"
    paternal_uncle_2_name = case_name+"TP2"
    alledged_paternal_uncle_1_name = case_name+"STP1"
    alledged_paternal_uncle_2_name = case_name+"STP2"
    another_1_name = case_name+"OUT1"
    another_2_name = case_name+"OUT2"

    mother = Subject(mother_name, [])
    child = Subject(child_name, [])
    child_2 = Subject(child_2_name, [])
    alledged_father = Subject(alledged_father_name, [])
    alledged_mother = Subject(alledged_mother_name, [])
    father = Subject(father_name, [])
    biologic_child_1 =  Subject(biologic_child_1_name, [])
    biologic_child_2 =  Subject(biologic_child_2_name, [])
    auxiliary_mother_1 =  Subject(auxiliary_mother_1_name, [])
    auxiliary_mother_2 =  Subject(auxiliary_mother_2_name, [])
    auxiliary_father_1 =  Subject(auxiliary_father_1_name, [])
    auxiliary_father_2 =  Subject(auxiliary_father_2_name, [])
    auxiliary_child_1_1 =  Subject(auxiliary_child_1_1_name, [])
    auxiliary_child_1_2 =  Subject(auxiliary_child_1_2_name, [])
    auxiliary_child_2_1 =  Subject(auxiliary_child_2_1_name, [])
    auxiliary_child_2_2 =  Subject(auxiliary_child_2_2_name, [])
    maternal_grandmother = Subject(maternal_grandmother_name, [])
    alledged_maternal_grandmother = Subject(alledged_maternal_grandmother_name, [])
    maternal_grandfather = Subject(maternal_grandfather_name, [])
    alledged_maternal_grandfather = Subject(alledged_maternal_grandfather_name, [])
    paternal_grandmother = Subject(paternal_grandmother_name, [])
    alledged_paternal_grandmother = Subject(alledged_paternal_grandmother_name, [])
    paternal_grandfather = Subject(paternal_grandfather_name, [])
    alledged_paternal_grandfather = Subject(alledged_paternal_grandfather_name, [])
    maternal_uncle_1 = Subject(maternal_uncle_1_name, [])
    maternal_uncle_2 = Subject(maternal_uncle_2_name, [])
    alledged_maternal_uncle_1 = Subject(alledged_maternal_uncle_1_name, [])
    alledged_maternal_uncle_2 = Subject(alledged_maternal_uncle_2_name, [])
    paternal_uncle_1 = Subject(paternal_uncle_1_name, [])
    paternal_uncle_2 = Subject(paternal_uncle_2_name, [])
    alledged_paternal_uncle_1 = Subject(alledged_paternal_uncle_1_name, [])
    alledged_paternal_uncle_2 = Subject(alledged_paternal_uncle_2_name, [])
    another_1 = Subject(another_1_name, [])
    another_2 = Subject(another_2_name, [])