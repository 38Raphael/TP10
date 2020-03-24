from Multinationale import Multinationale
#  from Employé import Employee
from Directeur import Directeur
from Administrator import Admninistrator
from Senior import Senior
from Junior import Junior
#  from Ingénieur import Ingenieur
from Filiale import Filiale
#  3.a
multi = Multinationale("RCAT", "la France")
#  3.b
fil1 = Filiale("RCAT-Belgique", "Belgique", 1938)
fil2 = Filiale("RCAT-Maroc", "Maroc", 1976)
fil3 = Filiale("RCAT-Tunisie", "Tunisie", 1995)
fil4 = Filiale("RCAT-Angleterre", "Angleterre", 1919)
multi.ajouterfiliale(fil3)
multi.ajouterfiliale(fil1)
multi.ajouterfiliale(fil2)
multi.ajouterfiliale(fil4)
#  3.c
dirl = Directeur("C'est moi", "le patron", 6, 133, 2008)
fil3.ajoutersal(dirl)
#  3.d
sal1 = Admninistrator("Kaboul", "le maboul", 2, 153, 2019, 253, "RH")
sal2 = Junior("J'adore la", "Belgique", 2, 122, 2020, 250, 303, 300, 2)
sal3 = Admninistrator("Moi", "Pas", 1, 154, 2017, 253, "Comptabilité")
sal4 = Senior("J'aime", "le Maroc", 2, 160, 2015, 253, 300, 300, "chef de l'équipe développement web")
fil3.ajoutersal(sal1)
fil1.ajoutersal(sal2)
fil1.ajoutersal(sal3)
fil2.ajoutersal(sal4)
#  3.e
multi.afficher()
#  3.f
fil3.supprsal(sal1)
#  3.g
multi.afficher()
#  3.h
fil2.supprsal(sal4)
fil1.ajoutersal(sal4)
#  3.i
multi.afficher()
