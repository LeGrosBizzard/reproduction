import threading
import requests
from bs4 import BeautifulSoup

#PARTIE PONCTUATION
from config.CONFIG import PONCTUATION
from config.CONFIG import PONCTUATION_ASSOCIATION
from config.CONFIG import PONCTUATION_OUT



#PARTIE VERBE

from config.CONFIG import PRONOM_PERSONNEL











#NE surtout pas écrire les print faut des truks qui le fasse

#un truk qui écrit du code

#ca inclus de lui dire quels ont été les étapes
#ca inclus de lui dire en détail les choses
#ensuite y mettre le truk vocal


#image cnn
#traitement de la parole lstl


GLOBAL = []
continuer = True
while continuer:


    def entree():

        #RAJOUTER UN PTS OU UN ?

        print("qui a fait la joconde ? et le radeau de la méduse ?")
        print("qui a fait la joconde?")
        print('qui a fais le radeau de la méduse ?')
        print("qui est l'auteur de la joconde")
        print("l'auteur de la joconde ?")
        print('qui est mona lisa ?')
        print('qui est le plus beau ?')
        print("est ce que je suis bete ?")
        print("quel temps fait il aujourdh'ui ?")
        print("que veut dire le mot 'pierre' ?")
        print('de quelle couleur est un poussin ?')
        print("Y a til du vert dans l'image ?")
        print("pourquoi pleut il ?")
        print("quand c'est les marchés de crest ?")
        print("pourquoi la terre est ronde ?")
        print("pourquoi je suis moche ?")
        print("combien de gens n'arrive pas à grimper a un arbre ? (jtm rachou)")
        
        print("\n\n")

        print('cherche moi un restaurant pres de chez moi')
        print("trouve l'adresse du concervatoire.")
        print("ou est le concervatoire ?")
        print("trouve la dérivée de x^2")


        print('fait moi un dessin')
        print("fais moi un poeme")
        #prend toutes les phrases on fait moyenne des phrases mot
        #on ressort lagencement
        

        print('envoie un mail')
        
        print("que veut dire en francais le mot stone")

        print("fais moi programme qui fait une table de mulitplication")
        print("corrige moi ce code stp")
        print("corrige moi ce texte stp")
        

        
        print("rajoute l'heure qu'il est dans la table de multiplication")
        print("qu'est ce qui différencie un chat d'un chien ?")

        
        print("résume moi ce texte")
        print("créer moi un environement virtuel, et un site sous django")
        print("le nombre de bouchons a crest")

        print("fais moi une analyse de l'image, trouves tu 5 balles par terre ? utilise le satellite, direction crest stp")
        
        print("")
        oInput = input('Que veux tu faire ?')
        
        return oInput






    def traitement_entree():
        """on split chaque mot"""

        entrance = entree()
        entrance = entrance.split()

        c = 0
        for i in entrance:
            mot = ""
            
            for j in i.lower():

                if j == "'":
                    mot += 'e'
                    GLOBAL.append(mot)
                    mot = ""
                    #On remplace l'auteur par le auteur


                else:
                    mot += j
      
            GLOBAL.append(mot)  





    from ponctuation.analyse_ponctuation_function import analyse_phrase
    from ponctuation.analyse_ponctuation_function import element_interro
    def analyse_ponctuation():
        """une question un ordre ?"""
        #ICI   Il va falloir savoir si continuité ou pas genre les virgules

        liste = analyse_phrase(GLOBAL, PONCTUATION)

        for i in liste:

            for j in i:
                for key, value in PONCTUATION_ASSOCIATION.items():
                    if j == key:
                        i.append(value)

        liste = element_interro(liste)

        return liste





    from config.CONFIG import PATH_VERBE
    def verbe():
        """Par les verbes on doit faire l'action"""

        liste_verbe = []

        for mot in GLOBAL:

            path = PATH_VERBE.format(mot)
            request_html = requests.get(path)
            page = request_html.content
            soup_html = BeautifulSoup(page, "html.parser")
            propriete = soup_html.find_all("td")

            for i in propriete:
                for pronom in PRONOM_PERSONNEL:
                    recherche = str(i).find(str(pronom))

                    if recherche >= 0:
                        liste_verbe.append([mot, pronom])
                        #on cherche je tu il nous vous ils


        return liste_verbe
        #DEUXIEME LISTE






    from nom.mot_cle_function import creation_par
    from nom.mot_cle_function import ville
    from nom.mot_cle_function import censure
    from nom.mot_cle_function import recherche_non_definition
    def mot_cle():
        """radeau de la méduse ?
        mona lisa ? ville ?
        """

        #ICI truk tableau, truk ville mais ville == ou?
        #qui a fait : (on attache avec +) stop a interro

        liste = analyse_phrase(GLOBAL, PONCTUATION)
        liste = censure(liste)
        
        liste1 = ["+".join(i) for i in liste]

        nom = creation_par(liste1, liste)


        non_mot_commun = []
        for i in liste:
            for j in i:
                non_mot = recherche_non_definition(j)
                if non_mot != "":
                    non_mot_commun.append(non_mot)


        nom_ville_ville = []
        for i in non_mot_commun:
            nom_ville = ville(i)
            nom_ville_ville.append(nom_ville)

            
        return nom, nom_ville_ville







    traitement_entree()


    #ponctuation = analyse_ponctuation()
    nom_commun = mot_cle()
    #vrb = verbe()





    #QUEL DAL ? question sur google.
    #et surtout qu'est ce qui est demaindé ?

##    print(GLOBAL)
##    print("\n\n")
##    print(ponctuation)
##    print("")
##    print(nom_commun)
##    print("")
##    print(vrb)
##    print("\n\n\n")










    from type_phrase.type_phrase import type_question
    def traitement_type_phrase(ponctuation):
        """question ? ordre ?
        question == qui que quoi quand pourquoi
        """

        
        type_phrase = ponctuation[-1]

        if type_phrase == "question":
            identification_question = type_question(ponctuation)

        

        



    from type_phrase.noms import identification_nom
    from type_phrase.noms import identification_pronom
    def traitement_des_nom(nom_commun, GLOBAL):

        
        #les_noms = identification_nom(nom_commun, GLOBAL)
        pronom = identification_pronom(GLOBAL)
        #return les_noms,
        return pronom


        
        #excla
        #ordre

        







    
    #type_phrase = traitement_type_phrase(ponctuation)
    #noms1 = traitement_des_nom(nom_commun, GLOBAL)
    pronom = traitement_des_nom(nom_commun, GLOBAL)

    #print(type_phrase)
    #print(noms1)
    print(pronom)













    #maintenant faut comprendre la question qui ? quand ? quoi ?
    #et la 3eme commencer a coder


    print("\n\n\n\n\n")
    cont = input("continuer maitre jb ?")
    if cont == "a":
        continuer = True
        GLOBAL = []
    else:
        print("arrivederci et va chez le coiffeur")
        print("ici tablea utrello")
        print("faut définir le temps ex quel temps hier/ojd")
        print("faut définir la place c'est comment je suis devenu gros, comment es tu devenu gros ?")
        print("marche plus pour double phrase")
        print("faut déterminer quoi est peint")
        print("marchés marche pas marché marche")


        print("ET LA PROGRAMMATION ORIENT2 OBJET __INIT__ ET TOUT")
        
        continuer = False




















