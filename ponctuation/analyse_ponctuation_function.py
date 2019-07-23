#faut documenté ca, mais plus tard ca te permettra de
#la connaitre par coeur

from config.CONFIG import ALPHABET
from config.CONFIG import FORME_INTERROGATIVE





def traitement_phrase(GLOBAL, PONCTUATION):

    liste = []
    presence = False
    

    for i in GLOBAL:

        c = 0
        oui = False
        ponctuationeze = False

        for j in i:
            
            for ponct in PONCTUATION:
                
                if j == ponct:
                    for lettre in ALPHABET:
                        
                        if lettre in (i[c - 1]) :
                            oui = True
                            
                    if oui is True:
                        liste.append(i[:-1])
                        liste.append(i[-1])
                        
                    else:
                        liste.append(i)

                    ponctuationeze = True
                    if ponct == "?":
                        presence = True
   
            c += 1

        if ponctuationeze is True:
            pass
        else:
            liste.append(i)


    return liste, presence





def no_ponctuation_question(GLOBAL):


    liste = []
    out = ""
    interro = False

    c = 0
    for i in GLOBAL:

        ok = False
        
        for cle, valeur in FORME_INTERROGATIVE.items():
            
            if i == cle:
                if c == valeur:
                    liste.append(cle)
                    ok = True
                    interro = True

        if ok is True:
            pass
        else:
            liste.append(i)

        c += 1

    if interro is True:
        liste.append("?")
        out = liste
    else:
        out = liste

    return out





def analyse_phrase(GLOBAL, PONCTUATION):
    """En gros on met les phrases dans une liste
    si virgule par exemple, faut analyser toutes les phrases"""

    GLOBAL, presence = traitement_phrase(GLOBAL, PONCTUATION)
    if presence is False:
        GLOBAL = no_ponctuation_question(GLOBAL)

        

    liste = []
    liste_w = []
    for i in GLOBAL:

        dont = False

        for ponct in PONCTUATION:
            if i == ponct:

                liste_w.append(i)
                liste.append(liste_w)
                dont = True

                liste_w = []

        if dont is True:
            pass
 
        else:
            liste_w.append(i)


    return liste






from config.CONFIG import FORME_INTERROGATIVE
def element_interro(liste):

    liste1 = []
    
    for i in liste:

        ok = False

        for j in i:
            for key, value in FORME_INTERROGATIVE.items():
                if j == key:
                    liste1.append(j)
                    ok = True

        if ok is True:
            pass
        else:
            liste1.append("")

    liste1.append("question")

    return liste1






































