from Salarié import Salarie


class Directeur(Salarie):
    def __init__(self, n2, p2, sa, i, year):
        Salarie.__init__(self, n2, p2, sa, i)
        self.__expyear = year

    def afficher(self):
        return "* [id=" + str(self._identifiant) + "] Nom et prénom: " + self._nomsalarie + " " + self._prenom + ", Salaire: " + str(self._salaire) + ", Statut: Directeur, Année de nomination: " + str(self.__expyear) + ", "
