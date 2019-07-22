def analyse_phrase(GLOBAL, PONCTUATION):
    """En gros on met les phrases dans une liste
    si virgule par exemple, faut analyser toutes les phrases"""

    liste = []
    liste_w = []#liste de Travail
    
    for i in GLOBAL:

        dont = False

        for ponct in PONCTUATION:
            if i == ponct:
                #On compare l'entrée avec la liste de PONCTUATION.
                
                liste_w.append(i)
                liste.append(liste_w)
                dont = True
                #On evite de mettre le symbole ponctu ds l'autre liste.
                
                liste_w = []
 
        if dont is True:
            pass
 
        else:
            liste_w.append(i)

    return liste

#GLOBAL = la question posée traité
#PONCTUATION les ponctuation
