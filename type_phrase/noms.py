import requests
from bs4 import BeautifulSoup



#quantités de personne







def bs4(i , PATH):
    
    path = PATH.format(i)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("span")
    return propriete



from config.CONFIG import PATH_NON_MOT
def identification_nom(nom_commun, GLOBAL):
    """on recupere le type (oeuvre ou ville)
    ainsi que l'entree en split"""


    #RETIRER ENCORE UNE FOIS LE PTS INTERRO
    #relier la fonction ici

    #et si y'a plusieurs oeuvre ou ville ne meme temps genre la scène ?
    #-> pas ok
    #attention au pluriel aussi -> ok
    #et au verbe -> ok

    liste = []

    for i in GLOBAL:
        propriete = bs4(i , PATH_NON_MOT)
        for pro in propriete:

            if pro.string == "Définitions corespondante à votre recherche":
                liste.append([i, nom_commun])
            
    return liste

    """Si on trouve pas de définition
    c'est que c'est une oeuvre ou une ville"""



#ET GENRE EUX ?
from config.CONFIG import DICO_PRONOM_PERSONNEL
def identification_pronom(GLOBAL):
    """direction le magazine virtuel x)"""

    liste = []
    
    for i in GLOBAL:
        for key, value in DICO_PRONOM_PERSONNEL.items():
            if i == key:
                index = GLOBAL.index(i)
                liste.append([value, index])

    return liste
    
































