import datetime

current_date = datetime.datetime.now()

#full_name = input("Nome completo: ").upper()
full_name = "Miguel Busarello Lauterjung".upper()
var = "1"
lab_case = "UD990000"
kit = "VE"

exclusion_test = ('\n\n\n'
        'CASO: ' + lab_case[0:4] + " " + lab_case[4:8] + '\n\n'
        'EXCLUSAO\n\n'
        'KIT A SER UTILIZADO:  (X) ' + kit + '\n\n'
        'PASTA: ' + lab_case[0:4] + ' ' + lab_case[4:8] + '_REP2_' + kit + '\n\n\n'
        'INDIVIDUOS A GENOTIPAR:\n\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'F_REP2_' + var + '\n'
        '\t\t\t\t' + lab_case[0:4] + ' ' + lab_case[4:8] + 'SP_REP2_' + var + '\n\n\n\n'
        '' + full_name + '\n'
        'LAGES SC, ' + current_date.strftime("%d %b %Y").upper())

print(exclusion_test)