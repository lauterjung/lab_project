from model.genotype import Genotype

gc = ["1", "2"]
gm = ["2", "3"]
gf = ["1", "2"]
gf = ["3", "4"]

# return Error if maternal mutation, or check for it before calculations
# relate gc, gm, gf and gg to Genotype class

def calc_trio(gc, gm, gf):
  # father doesn't share allele
    if any(allele not in gf for allele in gc):
        return 0
    
    # which allele came from mother? 
    if gc[0] == gc[1]:
        al_cm = [allele for allele in gc if allele in gm][0]
    else: # child iJ
        if len([allele for allele in gc if allele in gm]) == 1:
            al_cm = [allele for allele in gc if allele in gm][0]
        else: # if sum == 2, child iJ, mother iJ 
            pi = get_allele_frequency(locus, gc[0])
            pj = get_allele_frequency(locus, gc[1])
            if gf[0] == gf[1] | len([allele for allele in gc if allele in gf]) == 2: # father ii or iJ
                return(1/(pi+pj))
            else: # father Jk
                return(1/(2*(pi+pj)))
 
    # then pi is allele from father
    if gc[0] == gc[1]:
        al_cf = gc[0]
    elif([allele for allele in gc if allele not in gm][0] in gf):
        al_cf = [allele for allele in gc if allele not in gm][0]
    else:
        return(0)  # if shared allele is not obliged paternal allele (OPA) 

    pi = get_allele_frequency(locus, al_cf)
    # father configuration
    if(gf[0] == gf[1]): #ii
        return(1/pi)
    else: #ij
        return(1/(2*pi)) # jk already included
    
def calc_duo(gc, gg):
    # father doesn't share allele
    if any(allele not in gg for allele in gc):
        return 0

    # gc = ii
    if gc[0] == gc[1]:
        pi = get_allele_frequency(locus, gc[0])
        
        if len([allele for allele in gc if allele in gg]) == 2: # gg = gc = ii
            return(1/pi)
        else: # gg = ij
            return(1/(2*pi))

    #gc = ij
    if len([allele for allele in gc if allele in gg]) == 1: #gg = ii ou ik
        pi = get_allele_frequency(locus, [allele for allele in gc if allele in gg][0])
    
        if gg[0] == gg[1]: # gg = ii
            return(1/(2*pi))
        else: # gg = ik
            return(1/(4*pi))
      
    else: # gg = ij
        pi = get_allele_frequency(locus, gc[0])
        pj = get_allele_frequency(locus, gc[1])
        return((pi+pj)/(4*pi*pj))