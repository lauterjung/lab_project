var = "1"
query = ('\n\n\n, ' + \
        'CASO: ' + var + " " + var + '\n\n' + \
        'EXCLUSAO\n\n,' + \
        'KIT A SER UTILIZADO:  (X) ' + var + '\n\n,' + \
        'PASTA: ' + var + ' ' + var + '_REP2_' + var + '\n\n\n,' + \
        'INDIVIDUOS A GENOTIPAR:\n\n,' + \
        '\t\t\t\t' + var + ' ' + var + 'F_REP2_' + var + '\n,' + \
        '\t\t\t\t' + var + ' ' + var + 'SP_REP2_' + var + '\n\n\n\n,' + \
        '' + var + '\n,' + \
        'LAGES SC, ' + var +'')

query = ('\n\n\n, '
        'CASO: ' + var + " " + var + '\n\n'
        'EXCLUSAO\n\n,'
        'KIT A SER UTILIZADO:  (X) ' + var + '\n\n,'
        'PASTA: ' + var + ' ' + var + '_REP2_' + var + '\n\n\n,'
        'INDIVIDUOS A GENOTIPAR:\n\n,'
        '\t\t\t\t' + var + ' ' + var + 'F_REP2_' + var + '\n,'
        '\t\t\t\t' + var + ' ' + var + 'SP_REP2_' + var + '\n\n\n\n,'
        '' + var + '\n,'
        'LAGES SC, ' + var +'')

pedido = "\n\n\n" +\
 "CASO: ", substr(caso, 1, 4), " ", substr(caso, 5, 8), "\n\n",
 "EXCLUSAO", "\n\n", 
 "KIT A SER UTILIZADO:  (X) ", kit_rep2, "\n\n",
 "PASTA:  ", substr(caso, 1, 4), " ", substr(caso, 5, 8), "_REP2_", kit_rep2, "\n\n\n",
 "INDIVIDUOS A GENOTIPAR:", "\n\n",
 "\t\t\t\t", substr(caso, 1, 4), " ", substr(caso, 5, 8), "F_REP2_", kit_rep2, "\n",
 "\t\t\t\t", substr(caso, 1, 4), " ", substr(caso, 5, 8), "SP_REP2_", kit_rep2, "\n\n\n\n",
 nome_completo, "\n",
 "LAGES SC, ", fdata)"
