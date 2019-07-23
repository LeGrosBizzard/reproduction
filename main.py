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
        print('qui a fais et le radeau de la méduse ?')
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
        print("pourquoi chui moche ?")

        
        print("\n\n\n\n")

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
    def mot_cle():
        """radeau de la méduse ?
        mona lisa ? ville ?
        """

        liste = analyse_phrase(GLOBAL, PONCTUATION)
        liste1 = ["+".join(i) for i in liste]

        nom = creation_par(liste1, liste)
        
        if nom == []:
            nom = []
            nom_w = []
            for i in GLOBAL:
                sortie = ville(i)
                if sortie != "" or sortie != None:
                    nom_w.append(sortie)

            for i in nom_w:
                if i != "ville":
                    pass
                else:
                    nom.append(i)
                    
                    #mettre un scrap genre et, les, quand
        
        return nom










    #on déduit si c'est une question

    #sur un nom du genre un tableau ?

    #et les verbes

    traitement_entree()


    ponctuation = analyse_ponctuation()
    nom_commun = mot_cle()
    vrb = verbe()








    #le temps de la phrase ?
    #je ? il ? tu ?
    #déduis puis efface les mots.
    #QUEL DAL ? question sur google.
    #et surtout qu'est ce qui est demaindé ?

    print(GLOBAL)
    print("\n\n")
    print(ponctuation)
    print("")
    print(nom_commun)
    print("")
    print(vrb)
    print("\n\n\n")



































    from type_phrase.question import type_question
    def traitement_type_phrase(ponctuation):
        """question ? ordre ?
        question == qui que quoi quand pourquoi
        """

        
        type_phrase = ponctuation[-1]
        print(type_phrase)
        
        if type_phrase == "question":
            type_question(ponctuation)

        
        
        #excla
        #ordre






    """les noms communs et combien par exemple ?"""
    type_phrase = traitement_type_phrase(ponctuation)
















    #maintenant faut comprendre la question qui ? quand ? quoi ?
    #et la 3eme commencer a coder



    cont = input("continuer maitre jb ?")
    if cont == "a":
        continuer = True
    else:
        print("arrivederci et va chez le coiffeur")
        print("ici tablea utrello")
        print("faut définir le temps ex quel temps hier/ojd")
        print("faut définir la place c'est comment je suis devenu gros, comment es tu devenu gros ?")

        print("les noms commun genre ronde//mona lisa....")


        continuer = False




















