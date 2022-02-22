import csv

from numpy import column_stack
from classes.locus import Locus
from controller.database import LocusDB


class AlleleFrequencyService:
    def __init__(self, db: LocusDB):
        self.db = db
        
    def read_allele_frequency(self, file):
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            lines = []
            for row in csv_reader:
                lines.append(row)
        
        # falta um if locus.name == name, porque locus já tá no db. Só lê a freq   
        # ou um método update()? 
        columns = zip(*lines)
        frequency_list = []
        for column in columns:
            frequency_list.append(column)
        d_keys = frequency_list[0][1:]
                
        for row in frequency_list[1:]:
            name = row[0].strip()
            alleles = {}
            for i, v in enumerate(frequency_list):
                try:
                    alleles[d_keys[i]] = float(row[1+i].replace(",", "."))
                except:
                    alleles[d_keys[i]] = 0.001
            new_locus = Locus(name)
            new_locus.alleles = alleles
            self.db.save(new_locus)