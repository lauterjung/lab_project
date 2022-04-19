from model.genotype import Genotype

child_alleles = ["1", "2"]
mother_alleles = ["2", "3"]
father_alleles = ["1", "2"]
father_alleles = ["3", "4"]

# return Error if maternal mutation, or check for it before calculations
# relate child_alleles, mother_alleles, father_alleles and gg to Genotype class

def calc_trio(child_alleles, mother_alleles, father_alleles) -> float:
  # father doesn't share allele
    if all(allele not in father_alleles for allele in child_alleles):
        return 0
    
    # which allele came from mother? 
    if child_alleles[0] == child_alleles[1]:
        al_cm = [allele for allele in child_alleles if allele in mother_alleles][0]
    else: # child iJ
        if len([allele for allele in child_alleles if allele in mother_alleles]) == 1:
            al_cm = [allele for allele in child_alleles if allele in mother_alleles][0]
        else: # if sum == 2, child iJ, mother iJ 
            pi = get_allele_frequency(locus, child_alleles[0])
            pj = get_allele_frequency(locus, child_alleles[1])
            if father_alleles[0] == father_alleles[1] | len([allele for allele in child_alleles if allele in father_alleles]) == 2: # father ii or iJ
                return(1/(pi+pj))
            else: # father Jk
                return(1/(2*(pi+pj)))
 
    # then pi is allele from father
    if child_alleles[0] == child_alleles[1]:
        al_cf = child_alleles[0]
    elif([allele for allele in child_alleles if allele not in mother_alleles][0] in father_alleles):
        al_cf = [allele for allele in child_alleles if allele not in mother_alleles][0]
    else:
        return(0)  # if shared allele is not obliged paternal allele (OPA) 

    pi = get_allele_frequency(locus, al_cf)
    # father configuration
    if(father_alleles[0] == father_alleles[1]): #ii
        return(1/pi)
    else: #ij
        return(1/(2*pi)) # jk already included
    
def calc_duo(child_alleles, gg) -> float:
    # father doesn't share allele
    if all(allele not in gg for allele in child_alleles):
        return 0

    # child_alleles = ii
    if child_alleles[0] == child_alleles[1]:
        pi = get_allele_frequency(locus, child_alleles[0])
        
        if len([allele for allele in child_alleles if allele in gg]) == 2: # gg = child_alleles = ii
            return(1/pi)
        else: # gg = ij
            return(1/(2*pi))

    #child_alleles = ij
    if len([allele for allele in child_alleles if allele in gg]) == 1: #gg = ii ou ik
        pi = get_allele_frequency(locus, [allele for allele in child_alleles if allele in gg][0])
    
        if gg[0] == gg[1]: # gg = ii
            return(1/(2*pi))
        else: # gg = ik
            return(1/(4*pi))
      
    else: # gg = ij
        pi = get_allele_frequency(locus, child_alleles[0])
        pj = get_allele_frequency(locus, child_alleles[1])
        return((pi+pj)/(4*pi*pj))