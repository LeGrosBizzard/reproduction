

#qui que quoi pourquoi ?


from config.CONFIG import EL_DICO
def type_question(ponctuation):

    out = []
    
    marqueur = [i for i in ponctuation if i != "question"]
    for i in marqueur:
        for cle, valeur in EL_DICO.items():
            if cle == i:
                out.append(valeur)

    
    return out
