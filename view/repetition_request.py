import datetime

current_date = datetime.datetime.now()

# full_name = input("Nome completo: ").upper()
full_name = "Miguel Busarello Lauterjung".upper()
lab_case = "UD990000"
kit = "VE"
locus = "CSFPO"
subject_1 = "F"
subject_2 = "SP"

exclusion_request = ('\n\n\n'
        'CASO: ' + lab_case[0:4] + " " + lab_case[4:8] + '\n\n'
        'EXCLUSÃO\n\n'
        'KIT A SER UTILIZADO:  (X) ' + kit + '\n\n'
        'PASTA: ' + lab_case[0:4] + ' ' + lab_case[4:8] + '_REP2_' + kit + '\n\n\n'
        'INDIVÍDUOS A GENOTIPAR:\n\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'F_REP2_' + kit + '\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'SP_REP2_' + kit + '\n\n\n\n'
        '' + full_name + '\n'
        'LAGES SC, ' + current_date.strftime("%d %b %Y").upper())

print(exclusion_request)

mutation_request = ('\n\n\n'
        'CASO: ' + lab_case[0:4] + " " + lab_case[4:8] + '\n\n'
        'MUTAÇÃO NO LOCO ' + locus + ' ENTRE ' + subject_1 + " E " + subject_2 + '\n\n'
        'KIT A SER UTILIZADO:  (X) ' + kit + '\n\n'
        'PASTA: ' + lab_case[0:4] + ' ' + lab_case[4:8] + '_REP2_' + kit + '\n\n\n'
        'INDIVIDUOS A GENOTIPAR:\n\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'M_REP2_' + kit + '\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'F_REP2_' + kit + '\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'SP_REP2_' + kit + '\n\n\n\n'
        '' + full_name + '\n'
        'LAGES SC, ' + current_date.strftime("%d %b %Y").upper())

print(mutation_request)