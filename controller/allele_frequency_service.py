import csv

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
        
        for i, column in enumerate(columns):
            if i == 0:
                allele_names = column[1:]
                print(allele_names)
                continue

            locus = Locus(column[0].strip())
            for j, frequency in enumerate(column[1:]):
                try:
                    locus.alleles[allele_names[j]] = float(frequency.replace(",", "."))
                except:
                    pass
                self.db.save(locus)