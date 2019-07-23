

PONCTUATION = ["?",".",",","'",'"',":","!"]
PONCTUATION_ASSOCIATION = {'?':'question'}
PONCTUATION_OUT = {'question':'réponse'}


PATH_VERBE = 'https://leconjugueur.lefigaro.fr/conjugaison/verbe/{}.html'

PRONOM_PERSONNEL = ['Première personne du singulier',
                    'Deuxième personne du singulier',
                    'Troisième personne du singulier',
                    'Première personne du pluriel',
                    'Deuxième personne du pluriel',
                    'Troisième personne du pluriel']



DICO_PRONOM_PERSONNEL = {
                        "je":'Première personne du singulier',
                        "tu":'Deuxième personne du singulier',
                        "il":'Troisième personne du singulier',
                        "elle":'Troisième personne du singulier',
                        "on":'Troisième personne du singulier',
                        "nous": 'Première personne du pluriel',
                        "vous" : 'Deuxième personne du pluriel',
                        "ils" : 'Troisième personne du pluriel',
                        "elles" : 'Troisième personne du pluriel'
                         }



PATH_OEUVRE = "https://www.google.com/search?ei=U2Q3XYbgD86LlwSc-bOgAg&q={0}&oq={0}&gs_l=psy-ab.3..35i39j0j0i22i30.13122.15614..15702...0.0..0.122.2072.6j14......0....1..gws-wiz.......0i71j0i131j0i67.KsSUEk1p6-M&ved=0ahUKEwjG1d2058vjAhXOxYUKHZz8DCQQ4dUDCAo&uact=5"
LISTE_OEUVRE = ["peinture", "peint","est un tableau", "livre"]


PATH_NON_MOT = "https://www.le-dictionnaire.com/definition/{0}"


ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"] 

FORME_INTERROGATIVE = {"qui": 0, "que": 0, "quoi": 1,
                       "quel": 1, "qu'": 1, "quand": 1,
                       "comment":0, "pourquoi":1}

#1 nimporte quelle place 0 au début


PATH_VILLE = "https://www.google.com/search?ei=Zzg2XceFEs6LlwSc-bOgAg&q={0}&oq={0}&gs_l=psy-ab.3..35i39l2j0i67l4j0i131l2j0i67j0.5977.6655..6772...0.0..0.108.514.1j4......0....1..gws-wiz.......0i71j0i131i67.GtyXEM9VuS8&ved=0ahUKEwiH1ZixycnjAhXOxYUKHZz8DCQQ4dUDCAo&uact=5"




EL_DICO = {"qui": "une personne", "pourquoi": "une cause",
           "quel": {"indirect" : "quantité chose ou personne",
                    "direct": "identité d'une personne"},
           "quelle": {"indirect" : "quantité chose ou personne",
                    "direct": "identité d'une personne"},
           "quand": "un moment"


           } 
            






























