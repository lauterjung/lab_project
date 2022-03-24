from model.genotype import Genotype
from model.lab_case import LabCase
from model.subject import Subject

class TestSetup():
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

    swapped_mother_name = case_name+"M"
    swapped_alledged_father_name = case_name+"SP"
    swapped_alledged_mother_name = case_name+"SM"
    swapped_father_name = case_name+"P"
    swapped_auxiliary_mother_1_name = case_name+"_1M"
    swapped_auxiliary_mother_2_name = case_name+"_2M"
    swapped_auxiliary_father_1_name = case_name+"_1P"
    swapped_auxiliary_father_2_name = case_name+"_2P"
    swapped_maternal_grandmother_name = case_name+"MM"
    swapped_alledged_maternal_grandmother_name = case_name+"SMM"
    swapped_maternal_grandfather_name = case_name+"PM"
    swapped_alledged_maternal_grandfather_name = case_name+"SPM"
    swapped_paternal_grandmother_name = case_name+"MP"
    swapped_alledged_paternal_grandmother_name = case_name+"SMP"
    swapped_paternal_grandfather_name = case_name+"PP"
    swapped_alledged_paternal_grandfather_name = case_name+"SPP"

    mother = Subject(mother_name, [])
    child = Subject(child_name, [])
    child_2 = Subject(child_2_name, [])
    alledged_father = Subject(alledged_father_name, [])
    alledged_mother = Subject(alledged_mother_name, [])
    father = Subject(father_name, [])
    biologic_child_1 = Subject(biologic_child_1_name, [])
    biologic_child_2 = Subject(biologic_child_2_name, [])
    auxiliary_mother_1 = Subject(auxiliary_mother_1_name, [])
    auxiliary_mother_2 = Subject(auxiliary_mother_2_name, [])
    auxiliary_father_1 = Subject(auxiliary_father_1_name, [])
    auxiliary_father_2 = Subject(auxiliary_father_2_name, [])
    auxiliary_child_1_1 = Subject(auxiliary_child_1_1_name, [])
    auxiliary_child_1_2 = Subject(auxiliary_child_1_2_name, [])
    auxiliary_child_2_1 = Subject(auxiliary_child_2_1_name, [])
    auxiliary_child_2_2 = Subject(auxiliary_child_2_2_name, [])
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

    swapped_mother = Subject(swapped_mother_name, [])
    swapped_alledged_father = Subject(swapped_alledged_father_name, [])
    swapped_alledged_father_duo = Subject(swapped_alledged_father_name, [])
    swapped_alledged_mother = Subject(swapped_alledged_mother_name, [])
    swapped_father = Subject(swapped_father_name, [])
    swapped_auxiliary_mother_1 = Subject(swapped_auxiliary_mother_1_name, [])
    swapped_auxiliary_mother_2 = Subject(swapped_auxiliary_mother_2_name, [])
    swapped_auxiliary_father_1 = Subject(swapped_auxiliary_father_1_name, [])
    swapped_auxiliary_father_2 = Subject(swapped_auxiliary_father_2_name, [])
    swapped_maternal_grandmother = Subject(swapped_maternal_grandmother_name, [])
    swapped_alledged_maternal_grandmother = Subject(swapped_alledged_maternal_grandmother_name, [])
    swapped_maternal_grandfather = Subject(swapped_maternal_grandfather_name, [])
    swapped_alledged_maternal_grandfather = Subject(swapped_alledged_maternal_grandfather_name, [])
    swapped_paternal_grandmother = Subject(swapped_paternal_grandmother_name, [])
    swapped_alledged_paternal_grandmother = Subject(swapped_alledged_paternal_grandmother_name, [])
    swapped_paternal_grandfather = Subject(swapped_paternal_grandfather_name, [])
    swapped_alledged_paternal_grandfather = Subject(swapped_alledged_paternal_grandfather_name, [])
    
    male_genotype = Genotype("VE", "Amel", "X", "Y")
    female_genotype = Genotype("VE", "Amel", "X", "X")
         
    child.genetic_profile.append(male_genotype)
    child_2.genetic_profile.append(male_genotype)
    biologic_child_1.genetic_profile.append(male_genotype)
    biologic_child_2.genetic_profile.append(male_genotype)
    auxiliary_child_1_1.genetic_profile.append(male_genotype)
    auxiliary_child_1_2.genetic_profile.append(male_genotype)
    auxiliary_child_2_1.genetic_profile.append(male_genotype)
    auxiliary_child_2_2.genetic_profile.append(male_genotype)
    maternal_uncle_1.genetic_profile.append(male_genotype)
    maternal_uncle_2.genetic_profile.append(male_genotype)
    alledged_maternal_uncle_1.genetic_profile.append(male_genotype)
    alledged_maternal_uncle_2.genetic_profile.append(male_genotype)
    paternal_uncle_1.genetic_profile.append(male_genotype)
    paternal_uncle_2.genetic_profile.append(male_genotype)
    alledged_paternal_uncle_1.genetic_profile.append(male_genotype)
    alledged_paternal_uncle_2.genetic_profile.append(male_genotype)
    another_1.genetic_profile.append(male_genotype)
    another_2.genetic_profile.append(male_genotype)

    mother.genetic_profile.append(female_genotype)
    alledged_father.genetic_profile.append(male_genotype)
    alledged_mother.genetic_profile.append(female_genotype)
    father.genetic_profile.append(male_genotype)
    auxiliary_mother_1.genetic_profile.append(female_genotype)
    auxiliary_mother_2.genetic_profile.append(female_genotype)
    auxiliary_father_1.genetic_profile.append(male_genotype)
    auxiliary_father_2.genetic_profile.append(male_genotype)
    maternal_grandmother.genetic_profile.append(female_genotype)
    alledged_maternal_grandmother.genetic_profile.append(female_genotype)
    maternal_grandfather.genetic_profile.append(male_genotype)
    alledged_maternal_grandfather.genetic_profile.append(male_genotype)
    paternal_grandmother.genetic_profile.append(female_genotype)
    alledged_paternal_grandmother.genetic_profile.append(female_genotype)
    paternal_grandfather.genetic_profile.append(male_genotype)
    alledged_paternal_grandfather.genetic_profile.append(male_genotype)

    swapped_mother.genetic_profile.append(male_genotype)
    swapped_alledged_father.genetic_profile.append(female_genotype)
    swapped_alledged_father_duo.genetic_profile.append(female_genotype)
    swapped_alledged_mother.genetic_profile.append(male_genotype)
    swapped_father.genetic_profile.append(female_genotype)
    swapped_auxiliary_mother_1.genetic_profile.append(male_genotype)
    swapped_auxiliary_mother_2.genetic_profile.append(male_genotype)
    swapped_auxiliary_father_1.genetic_profile.append(female_genotype)
    swapped_auxiliary_father_2.genetic_profile.append(female_genotype)
    swapped_maternal_grandmother.genetic_profile.append(male_genotype)
    swapped_alledged_maternal_grandmother.genetic_profile.append(male_genotype)
    swapped_maternal_grandfather.genetic_profile.append(female_genotype)
    swapped_alledged_maternal_grandfather.genetic_profile.append(female_genotype)
    swapped_paternal_grandmother.genetic_profile.append(male_genotype)
    swapped_alledged_paternal_grandmother.genetic_profile.append(male_genotype)
    swapped_paternal_grandfather.genetic_profile.append(female_genotype)
    swapped_alledged_paternal_grandfather.genetic_profile.append(female_genotype)
    
    correct_case_trio = LabCase(case_name)
    correct_case_trio.subjects.extend([mother, child, alledged_father])
    swapped_case_trio = LabCase(case_name)
    swapped_case_trio.subjects.extend([swapped_mother, child, alledged_father])
    swapped_case_trio_2 = LabCase(case_name)
    swapped_case_trio_2.subjects.extend([swapped_mother, child, swapped_alledged_father])
    
    correct_case_duo = LabCase(case_name)
    correct_case_duo.subjects.extend([child, alledged_father])
    swapped_case_duo = LabCase(case_name)
    swapped_case_duo.subjects.extend([child, swapped_alledged_father_duo])

    no_gender_case_complex = LabCase(case_name)
    no_gender_case_complex.subjects.extend([child, paternal_uncle_1, maternal_uncle_1, another_1])

    # check_swap_trio
    vWA_1_2 = Genotype("VE", "vWA", "1", "2")
    vWA_1_3 = Genotype("VE", "vWA", "1", "3")
    vWA_1_4 = Genotype("VE", "vWA", "1", "4")
    vWA_2_3 = Genotype("VE", "vWA", "2", "3")
    vWA_2_4 = Genotype("VE", "vWA", "2", "4")
    vWA_3_4 = Genotype("VE", "vWA", "3", "4")
    FGA_1_2 = Genotype("VE", "FGA", "1", "2")
    FGA_1_3 = Genotype("VE", "FGA", "1", "3")
    FGA_1_4 = Genotype("VE", "FGA", "1", "4")
    FGA_1_9 = Genotype("VE", "FGA", "1", "9")
    FGA_2_3 = Genotype("VE", "FGA", "2", "3")
    FGA_2_4 = Genotype("VE", "FGA", "2", "4")
    FGA_3_4 = Genotype("VE", "FGA", "3", "4")
    FGA_9_9 = Genotype("VE", "FGA", "9", "9")
    CSFPO_1_2 = Genotype("VE", "CSFPO", "1", "2")
    CSFPO_1_3 = Genotype("VE", "CSFPO", "1", "3")
    CSFPO_1_4 = Genotype("VE", "CSFPO", "1", "4")
    CSFPO_2_3 = Genotype("VE", "CSFPO", "2", "3")
    CSFPO_2_4 = Genotype("VE", "CSFPO", "2", "4")
    CSFPO_3_4 = Genotype("VE", "CSFPO", "3", "4")
    TPOX_1_2 = Genotype("VE", "TPOX", "1", "2")
    TPOX_1_3 = Genotype("VE", "TPOX", "1", "3")
    TPOX_1_9 = Genotype("VE", "TPOX", "1", "9")
    TPOX_2_3 = Genotype("VE", "TPOX", "2", "3")
    TPOX_2_4 = Genotype("VE", "TPOX", "2", "4")
    TPOX_3_4 = Genotype("VE", "TPOX", "3", "4")
    TPOX_9_9 = Genotype("VE", "TPOX", "9", "9")

    child1 = Subject(child_name, [female_genotype, vWA_1_2, FGA_1_2, CSFPO_1_2, TPOX_1_2])
    mother1 = Subject(mother_name, [female_genotype, vWA_1_2, FGA_1_2, CSFPO_1_2, TPOX_1_2])
    mother2 = Subject(mother_name, [female_genotype, vWA_1_2, FGA_1_2, CSFPO_1_3, TPOX_1_3])
    mother3 = Subject(mother_name, [female_genotype, vWA_1_3, FGA_1_3, CSFPO_1_3, TPOX_1_3])
    mother4 = Subject(mother_name, [female_genotype, vWA_1_2, FGA_1_2, CSFPO_3_4, TPOX_3_4])
    mother5 = Subject(mother_name, [female_genotype, vWA_3_4, FGA_3_4, CSFPO_3_4, TPOX_3_4])
    mother6 = Subject(mother_name, [female_genotype, vWA_3_4, FGA_1_4, CSFPO_1_4, TPOX_1_2])
    mother7 = Subject(mother_name, [female_genotype, vWA_1_2, FGA_1_2, CSFPO_1_4, TPOX_1_9])
    mother8 = Subject(mother_name, [female_genotype, vWA_1_3, FGA_1_9, CSFPO_1_4, TPOX_1_9])
    alledged_father1 = Subject(alledged_father_name, [male_genotype, vWA_1_2, FGA_1_2, CSFPO_1_2, TPOX_1_2])
    alledged_father2 = Subject(alledged_father_name, [male_genotype, vWA_1_2, FGA_1_2, CSFPO_2_4, TPOX_2_4])
    alledged_father3 = Subject(alledged_father_name, [male_genotype, vWA_2_4, FGA_2_4, CSFPO_2_4, TPOX_2_4])
    alledged_father4 = Subject(alledged_father_name, [male_genotype, vWA_1_2, FGA_1_2, CSFPO_1_4, TPOX_9_9])
    alledged_father5 = Subject(alledged_father_name, [male_genotype, vWA_1_4, FGA_9_9, CSFPO_1_4, TPOX_9_9])
    alledged_father6 = Subject(alledged_father_name, [male_genotype, vWA_1_4, FGA_3_4, CSFPO_2_3, TPOX_1_2])
    alledged_father7 = Subject(alledged_father_name, [male_genotype, vWA_1_2, FGA_1_2, CSFPO_2_3, TPOX_2_3])
    alledged_father8 = Subject(alledged_father_name, [male_genotype, vWA_2_3, FGA_2_3, CSFPO_2_3, TPOX_2_3])

    case_000 = LabCase(case_name)
    case_200 = LabCase(case_name)
    case_400 = LabCase(case_name)
    case_020 = LabCase(case_name)
    case_040 = LabCase(case_name)
    case_002 = LabCase(case_name)
    case_004 = LabCase(case_name)
    case_111 = LabCase(case_name)

    case_000.subjects.extend([child1, mother1, alledged_father1])
    case_200.subjects.extend([child1, mother2, alledged_father2])
    case_400.subjects.extend([child1, mother3, alledged_father3])
    case_020.subjects.extend([child1, mother4, alledged_father7])
    case_040.subjects.extend([child1, mother5, alledged_father8])
    case_002.subjects.extend([child1, mother7, alledged_father4])
    case_004.subjects.extend([child1, mother8, alledged_father5])
    case_111.subjects.extend([child1, mother6, alledged_father6])