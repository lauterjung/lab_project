gc = ["1", "1"]
gm = ["1", "2"]
gf = ["1", "2"]
# gf = ["3", "4"]

def calc_trio(gc, gm, gf):

  # caso o pai não compartilha nenhum alelo  
    if any(allele in gc for allele in gf):
        return 0

  # qual alelo veio da mãe?  
    if gc[0] == gc[1]:
        al_cm = [allele for allele in gc if allele in gm][0]
    else: # criança iJ
  
        if len([allele for allele in gc if allele in gm]) == 1:
            al_cm = [allele for allele in gc if allele in gm][0]
        else: # caso de soma 2, criança iJ, mãe iJ #if(sum(gc %in% gm)==2) 
    
            pi = get.freq(gc[0],locus=locus, allele.freq)
            pj = get.freq(gc[1],locus=locus, allele.freq)
            
            if gf[0] == gf[1] | len([allele for allele in gc if allele in gf]) == 2: #pai ii ou iJ
                return(1/(pi+pj))
            else: # pai Jk
                return(1/(2*(pi+pj)))
    
    #então o alelo do pai é o pi
    if gc[0] == gc[1]:
        al_cf = gc[0]
    else:
    if(gc[gc!=al.cm] %in% gf){
    al.cf <- gc[gc!=al.cm]
    } else{
    return(0)  #caso o pai possua um alelo em comum, mas não é o APO 
    }
  }
    
  pi <- get.freq(al.cf, locus = locus, allele.freq)
  
  #qual a configuração do pai?
  if(gf[1]==gf[2]){ #ii
  return(1/pi)
  } else{ #ij
    return(1/(2*pi))
  } #jk já foi tratado

}


for a in gc:
    if a in gm:
        res = a
        
for a in gm:
    if a in gc:
        res = a

a for a in gm if a in gc

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 

a in gc for a in gf

res = [a for a in gc if a in gm] 
res = [a for a in gm if a in gc][0]

 if(sum(gc %in% gm)==1)
 
 