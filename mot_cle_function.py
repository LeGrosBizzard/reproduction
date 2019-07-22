import requests
from bs4 import BeautifulSoup

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
    
    for i in terme:
        path = PATH_WIKIPEDIA.format(i)
        request_html = requests.get(path)
        page = request_html.content
        soup_html = BeautifulSoup(page, "html.parser")
        propriete = soup_html.find("div", {"class":"searchresult"})

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

    return liste_w













































