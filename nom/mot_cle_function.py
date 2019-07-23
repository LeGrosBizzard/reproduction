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
        
    return propriete




from nom.config.CONFIG import PATH_OEUVRE
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

    dico = {}
    
    for i in liste:
        for j in i:
            dico[j] = 0
        
    liste_w = []

    out = []

    for i in liste:
        
        propriete = bs4(i, PATH_OEUVRE.format(terme), "creation")

        
        for tag in propriete:
            
            try:
                for j in i:
                    variable = tag.string.lower()
                    find = str(variable).find(str(j))
                    if find >= 0:
                        dico[j] += 1
            except:
                pass

    for cle, valeur in dico.items():
        if valeur >= 20:
            out.append(cle)

    return out









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

            if finding >= 0 or\
               finding1 >= 0 or\
               finding2 >= 0 or\
               finding3 >= 0 or\
               finding4 >= 0:
                count += 1
                
            if count >= 4:
                out = "ville"
                return out

            
        except:
            out = ""
            return out

        
    









































