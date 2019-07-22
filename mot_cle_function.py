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
        propriete = soup_html.find("div", {"class":"searchresult"})
        
    elif mode == "ville":
        propriete = soup_html.find_all("div")
        
    return propriete



def creation_par(terme, liste, PATH_WIKIPEDIA):
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

    
    liste_w = []
    out = ""

    for i in terme:
        
        propriete = bs4(i, PATH_WIKIPEDIA, "creation")


        try:
            variable_w = propriete.get_text().lower().split()
            #on recup text, on le lower et le split

            for i in liste:

                liste3 = []
                for element in i:
                    if (element in variable_w):
                        if element in ("le", "la", "de", "des", "les", "et"):
                            pass
                        else:
                            liste3.append(element)

                liste_w.append(liste3)
                liste_w = verification_creation_par(liste3)
                
            out = liste_w
        except:
            out = ""

    return out


from CONFIG import PATH_VILLE
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

        
    









































