import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


def verification_creation_par(liste3):

    liste = []

    for i in liste3:
        if len(i) < 3:
            pass
        else:
            liste.append(i)

    return liste


def bs4(i, PATH, mode):
    
    path = PATH.format(i)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    
    if mode == "creation":
        propriete = soup_html.find_all("div")

    elif mode == "ville":
        propriete = soup_html.find_all("div")
        
    elif mode == "mot":
        propriete = soup_html.find_all("span")

    return propriete



from config.CONFIG import LISTE_OEUVRE
def censure(terme):

    liste = []

    for mot in terme[0]:

        ok = False
        
        for i in LISTE_OEUVRE:
            if mot == i:
                liste.append("fait")
                ok = True
        if ok is True:
            pass
        else:
            liste.append(mot)

    return [liste]



from config.CONFIG import PATH_OEUVRE
from config.CONFIG import LISTE_OEUVRE
def creation_par(terme, liste):
    """En gros la tu:
    scrap sur wiki si l'entrée est présente,
    on récup le premier article,
    on compare l'entree avec lartcile (cad les mot qui corresponde)
    si y'a un match alors
    on déduit que c le nom d'une creation ex: la joconde ou
    le radeau de la méduse
    bien sur si on cherche quel couleur voiture
    donc ensuite faut passer ca au dico qui éliminera les mots
    ex: voiture trouvé, joconde non trouvé donc créa
    ps: on supprime les le la ect... apres un ptit wiki on récu
    perera les le la les"""


    if terme[0][-1] == "?":
        terme = terme[0][:-1]

    #print(PATH_OEUVRE.format(terme))

    propriete = bs4(terme, PATH_OEUVRE.format(terme), "creation")

    liste1 = []
    
    for i in propriete:

        for element in LISTE_OEUVRE:
            
            finding = str(i.get_text().lower()).find(str(element))
            
            if finding >= 0:
                return ["oeuvre"]

##    for i in propriete:
##        for element in LISTE_PERSONNE:
##            finding = str(i.get_text().lower()).find(str(element))
##            if finding >= 0:
##                return "oeuvre"
    



from config.CONFIG import PATH_NON_MOT
def recherche_non_definition(mot):
    
    propriete = bs4(mot, PATH_NON_MOT, "mot")

    count = 0
    for i in propriete:
        if i.string == "Définitions corespondante à votre recherche":
            count += 1

    if count >= 1:
        return mot
    
    else:
        return ""



from config.CONFIG import PATH_VILLE
def ville(terme):
    """on cherche si ya des coordonées si oui c un ville
    si un tableau porte le nom d'une ville frere lache ton oinj,
    fait tournée, et remue toi ptin
    """

    count = 0

    propriete = bs4(terme, PATH_VILLE, "ville")
    for i in propriete:
        try:
            finding = str(i).find("ville de" + terme)
            finding1 = str(i).find("Ville de" + terme)
            finding2 = str(i).find(terme + " ville")
            finding3 = str(i).find(terme + " Ville")
            finding4 = str(i).find("Code postal de" + terme)
            finding5 = str(i).find("vivre à" + terme)
            finding6 = str(i).find(terme + " meteo") 
            finding7 = str(i).find(terme + " code postal")
            finding8 = str(i).find(terme + " restaurant")
            

            if finding >= 0 or\
               finding1 >= 0 or\
               finding2 >= 0 or\
               finding3 >= 0 or\
               finding4 >= 0 or\
               finding5 >= 0 or\
               finding6 >= 0 or\
               finding7 >= 0 or\
               finding8 >= 0:
                count += 1

            if count >= 4:
                out = ["ville", terme]
                return out

            
        except:
            out = ""
            return out

        
    









































