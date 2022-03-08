import csv

from model.locus import Locus
from controller.database import LocusDB


class AlleleFrequencyService:
    def __init__(self, db: LocusDB) -> None:
        self.db = db
        
    def read_allele_frequency(self, file) -> None:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            lines = []
            for row in csv_reader:
                lines.append(row)
            
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
        
    def get_allele_frequency(self, locus_name, allele_name) -> float:
        locus = self.db.fetch(locus_name)
        if locus != None:
            if allele_name in locus.alleles:
                return locus.alleles[allele_name]
            
        return 0.001

        