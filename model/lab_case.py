from model.subject import Subject

class LabCase:
    id: int
    juridic_cases: list[str]
    card_numbers: list[str]
        
    def __init__(self,  name: str, subjects: list[Subject] = []):
        self.name = name
        self.subjects = subjects

    def type_of_case(self):
        pass
        # for subject in self.subjects:
        #     if subject.type == "F": # como acessar direto os subject types pra verificar se "F in names"?
        #         continue
        #     else:
        #         # Raise error: F not found
        #         break
        # if len(self.subjects) > x:
 
        # return type_of_case
        # DUO
        # TRIO
        # COMPLEX
        
# old code (R) for basis
        
# tipo.caso <- ""
#   if(length(unique(dados$nomenclatura)) == 3 & # se não tiver essa linha, duo entra como trio
# 	 all(unique(dados$nomenclatura) %in% c("M", "F", "SP"))){
#     tipo.caso <- "Trio"
#   } 
  
#   if(length(unique(dados$nomenclatura)) == 2 &
# 	(all(unique(dados$nomenclatura) %in% c("F", "SP"))|
#   all(unique(dados$nomenclatura) %in% c("F", "SM")))){
#     tipo.caso <- "Duo"
#   } 

#   if(tipo.caso != "Trio" & tipo.caso != "Duo"){ 
#     tipo.caso <- "Complexo"
#   } 